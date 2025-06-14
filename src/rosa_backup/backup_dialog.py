from collections.abc import Callable
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import QProcess, QThread, Signal
from PySide6.QtWidgets import QDialog

from .config_manager import ConfigManager
from .UIs.BackupingDialog import Ui_Dialog


class BackupThread(QThread):
    backup_log_signal = Signal(str)

    def __init__(self, filepath: str, paths: list[str]) -> None:
        """
        Инициализирует поток резервного копирования.

        :param dialog: Экземпляр класса BackupDialog.
        """
        super(BackupThread, self).__init__()
        self.filepath = filepath
        self.paths = paths
        self.exit_code = 0

    def run(self):
        """
        Запускает процесс резервного копирования, активируя диалог.
        """
        process = QProcess()
        process.readyReadStandardOutput.connect(
            lambda: self.backup_log_signal.emit(
                bytes(process.readAllStandardOutput().data()).decode().strip()
            )
        )
        process.readyReadStandardError.connect(
            lambda: self.backup_log_signal.emit(
                bytes(process.readAllStandardError().data()).decode().strip()
            )
        )
        process.start("tar", ["cvzf", self.filepath, *self.paths])
        process.waitForFinished(2147483647)
        self.exit_code = process.exitCode()


class BackupDialog(QDialog):
    def __init__(
        self,
        filepath: Path,
        paths: list[str],
        config_manager: ConfigManager,
        update_table: Callable[[], None],
    ) -> None:
        """
        Инициализирует BackupDialog с указанными filepath и config_manager.

        :param filepath: Строка, представляющая путь к файлу.
        :param config_manager: Экземпляр ConfigManager.
        """
        super(BackupDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.name_text.setText(filepath.name)

        self.backup_thread = BackupThread(str(filepath), paths)

        self.backup_thread.backup_log_signal.connect(self.on_backup_log)
        self.backup_thread.finished.connect(self.on_backup_finish)

        self.config_manager = config_manager
        self.update_table = update_table

        self.ui.close_btn.clicked.connect(self.close)
        self.filepath = filepath

        self.backup_thread.start()
        self.exec()

    def on_backup_log(self, log: str) -> None:
        self.ui.textEdit.append(log)

    def start_backup(self) -> None:
        if not self.filepath:
            self.ui.close_btn.setEnabled(True)
            self.ui.textEdit.append("Выбран неверный путь")
            return
        self.backup_thread.backup_log_signal.emit(self.filepath)
        self.ui.name_text.setText(self.filepath.name)

    def on_backup_finish(self) -> None:
        try:
            file_size = self.filepath.stat().st_size
        except (
            FileNotFoundError
        ):  # Проверка на наличие резервной копии после завершения
            self.ui.close_btn.setEnabled(True)
            self.ui.textEdit.append("Oшибка создания резервной копии")
            return

        if self.backup_thread.exit_code != 0:  # Проверка статуса резервной копии
            self.ui.textEdit.append("Oшибка создания резервной копии")
            return
        
        self.config_manager.add_backup(  # Добавление записи о резервной копии в базу данных
            self.filepath.name,
            str(self.filepath),
            datetime.now().isoformat(),
            file_size,
        )
        self.ui.close_btn.setEnabled(True)
        self.ui.textEdit.append("Готово")
        self.update_table()
