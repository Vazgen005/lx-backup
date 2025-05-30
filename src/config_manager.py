import sqlite3
import threading
from getpass import getuser
from pathlib import Path
from typing import Any, Dict, List


class ConfigManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, db_path: str = "data.db"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ConfigManager, cls).__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self, db_path: str = "data.db") -> None:
        if self._initialized:
            return
        self._initialized = True
        self.db_path = db_path
        self._local = threading.local()
        self._initialize_db()

    def _get_conn(self):
        if not hasattr(self._local, "conn"):
            self._local.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            self._local.conn.row_factory = sqlite3.Row
        return self._local.conn

    def _get_cursor(self):
        conn = self._get_conn()
        if not hasattr(self._local, "cursor"):
            self._local.cursor = conn.cursor()
        return self._local.cursor

    def _initialize_db(self) -> None:
        """Инициализирует базу данных, если она не существует."""
        cursor = self._get_cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                autobackup BOOLEAN NOT NULL,
                interval_combo_index INTEGER NOT NULL,
                def_path TEXT NOT NULL,
                def_name TEXT NOT NULL,
                compress BOOLEAN NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS backups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                filepath TEXT NOT NULL,
                date TEXT NOT NULL,
                size INTEGER NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS paths (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT NOT NULL
            )
        """)

        # Проверяем, есть ли настройки в базе
        cursor.execute("SELECT COUNT(*) FROM settings")
        if cursor.fetchone()[0] == 0:
            # Добавляем настройки по умолчанию
            default_path = f"/home/{getuser()}/backups"
            cursor.execute(
                """
                INSERT INTO settings (autobackup, interval_combo_index, def_path, def_name, compress)
                VALUES (?, ?, ?, ?, ?)
            """,
                (False, 0, default_path, "backup-%d.%m.%Y-%H:%M:%S.tar.gz", True),
            )
            self._get_conn().commit()

    @property
    def config(self) -> dict[str, Any]:
        """Возвращает текущую конфигурацию в виде словаря."""
        settings = self._get_settings()
        backups = self.get_backups()
        return {"settings": settings, "backups": backups}
    
    def remove_path_by_id(self, id: int) -> None:
        cursor = self._get_cursor()
        cursor.execute("DELETE FROM paths WHERE id = ?", (id,))
        self._get_conn().commit()

    def add_path(self, path: str) -> None:
        """Добавляет новый путь в базу данных."""
        cursor = self._get_cursor()
        cursor.execute("INSERT INTO paths (path) VALUES (?)", (path,))
        self._get_conn().commit()

    def set_all_paths(self, paths: list[str]) -> None:
        cursor = self._get_cursor()
        cursor.execute("DELETE FROM paths")
        for path in paths:
            cursor.execute("INSERT INTO paths (path) VALUES (?)", (path,))
        self._get_conn().commit()

    def get_all_paths(self) -> list[str]:
        """Возвращает список всех путей."""
        cursor = self._get_cursor()
        cursor.execute("SELECT path FROM paths")
        return [row["path"] for row in cursor.fetchall()]

    def _get_settings(self) -> Dict[str, Any]:
        """Возвращает настройки из базы данных."""
        cursor = self._get_cursor()
        cursor.execute(
            "SELECT autobackup, interval_combo_index, def_path, def_name, compress FROM settings LIMIT 1"
        )
        row = cursor.fetchone()
        if row is None:
            raise ValueError("Settings table is empty")
        return {
            "autobackup": bool(row["autobackup"]),
            "interval_combo_index": row["interval_combo_index"],
            "def_path": row["def_path"],
            "def_name": row["def_name"],
            "compress": bool(row["compress"]),
        }

    def _update_settings(self, **kwargs) -> None:
        """Обновляет настройки в базе данных."""
        cursor = self._get_cursor()
        query = "UPDATE settings SET "
        query += ", ".join([f"{key} = ?" for key in kwargs.keys()])
        cursor.execute(query, tuple(kwargs.values()))
        self._get_conn().commit()

    def add_backup(self, filename: str, filepath: str, date: str, size: int) -> None:
        """
        Добавляет запись о резервной копии в базу данных.

        :param filename: str - имя файла резервной копии
        :param filepath: str - путь к файлу резервной копии
        :param date: str - дата создания резервной копии
        :param size: int - размер файла резервной копии
        """
        cursor = self._get_cursor()
        cursor.execute(
            """
            INSERT INTO backups (filename, filepath, date, size)
            VALUES (?, ?, ?, ?)
        """,
            (filename, filepath, date, size),
        )
        self._get_conn().commit()

    @property
    def autobackup(self) -> bool:
        """Возвращает значение авто-бэкапа."""
        return bool(self._get_settings()["autobackup"])

    @autobackup.setter
    def autobackup(self, value: bool) -> None:
        """Устанавливает значение авто-бэкапа."""
        self._update_settings(autobackup=int(value))

    @property
    def interval(self) -> int:
        """Возвращает индекс интервала."""
        return self._get_settings()["interval_combo_index"]

    @interval.setter
    def interval(self, value: int) -> None:
        """Устанавливает индекс интервала."""
        self._update_settings(interval_combo_index=value)

    @property
    def def_path(self) -> str:
        """Возвращает путь по умолчанию."""
        return self._get_settings()["def_path"]

    @def_path.setter
    def def_path(self, value: str) -> None:
        """Устанавливает путь по умолчанию."""
        self._update_settings(def_path=value)

    @property
    def def_name(self) -> str:
        """Возвращает шаблон имени по умолчанию."""
        return self._get_settings()["def_name"]

    @def_name.setter
    def def_name(self, value: str) -> None:
        """Устанавливает шаблон имени по умолчанию."""
        self._update_settings(def_name=value)

    def rename_backup(self, row: int, new_path: Path) -> None:
        """Переименовывает резервную копию."""
        backup_id = self._get_backup_id_by_row(row)
        cursor = self._get_cursor()
        cursor.execute(
            """
            UPDATE backups 
            SET filename = ?, filepath = ? 
            WHERE id = ?
        """,
            (new_path.name, str(new_path), backup_id),
        )
        self._get_conn().commit()

    def _get_backup_id_by_row(self, row: int) -> int:
        """Возвращает ID резервной копии по номеру строки."""
        cursor = self._get_cursor()
        cursor.execute("SELECT id FROM backups ORDER BY id LIMIT 1 OFFSET ?", (row,))
        result = cursor.fetchone()
        if result:
            return result["id"]
        raise IndexError("Backup row not found")

    def remove_backup(self, row: int) -> dict[str, Any]:
        """Удаляет резервную копию и возвращает информацию о ней."""
        backup_id = self._get_backup_id_by_row(row)
        cursor = self._get_cursor()

        # Получаем информацию о бэкапе перед удалением
        cursor.execute(
            "SELECT filename, filepath, date, size FROM backups WHERE id = ?",
            (backup_id,),
        )
        backup_info = cursor.fetchone()

        # Удаляем бэкап
        cursor.execute("DELETE FROM backups WHERE id = ?", (backup_id,))
        self._get_conn().commit()

        return {
            "filename": backup_info["filename"],
            "filepath": backup_info["filepath"],
            "date": backup_info["date"],
            "size": backup_info["size"],
        }

    def get_backups(self) -> List[Dict[str, Any]]:
        """Возвращает список всех резервных копий."""
        cursor = self._get_cursor()
        cursor.execute("SELECT filename, filepath, date, size FROM backups ORDER BY id")
        return [
            {
                "filename": row["filename"],
                "filepath": row["filepath"],
                "date": row["date"],
                "size": row["size"],
            }
            for row in cursor.fetchall()
        ]

    def get_backups_count(self) -> int:
        """Возвращает количество резервных копий."""
        cursor = self._get_cursor()
        cursor.execute("SELECT COUNT(*) FROM backups")
        return cursor.fetchone()[0]
    
    @property
    def compress(self) -> bool:
        return bool(self._get_settings()["compress"])

    @compress.setter
    def compress(self, value: bool) -> None:
        self._update_settings(compress=int(value))

    def close(self):
        """Закрывает все соединения с базой данных."""
        if hasattr(self._local, "conn"):
            self._local.conn.close()
            del self._local.conn
        if hasattr(self._local, "cursor"):
            del self._local.cursor

    def __del__(self):
        self.close()
