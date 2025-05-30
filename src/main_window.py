from functools import partial
import os
from datetime import datetime
from os.path import getsize
from pathlib import Path

import human_readable
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QItemDelegate,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStyle,
    QTableWidgetItem,
    QCheckBox,
    QHeaderView
)

from auto_backup import AutoBackup
from backup_dialog import BackupDialog
from config_manager import ConfigManager
from folder_selection import FolderSelection
from restore_dialog import RestoreDialog
from UIs.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, config_manager: ConfigManager):
        """
        Инициализирует главное окно с данным ConfigManager.
        Подключает кнопки к соответствующим функциям, настраивает
        QItemDelegate для таблицы резервных копий, инициализирует
        экземпляр AutoBackup с данным ConfigManager. Восстанавливает
        конфигурацию, обновляет таблицу и подгоняет размеры столбцов
        под содержимое.
        """
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.backups_table.horizontalHeader().setSectionResizeMode(
            0,QHeaderView.ResizeMode.ResizeToContents
        )

        self.config_manager = config_manager
        self.path_list: list[str] = []

        self.ui.backup_btn.clicked.connect(self.start_manual_backup)
        self.ui.path_button.clicked.connect(
            lambda: self.browse_folder(self.ui.path_input)
        )
        self.ui.def_path_button.clicked.connect(
            lambda: self.browse_folder(self.ui.def_path_input)
        )
        self.ui.backups_list_update_btn.clicked.connect(self.update_table)
        self.ui.save_autobackup_settings_btn.clicked.connect(self.save_config)

        self.ui.add_paths_btn.clicked.connect(self.select_backup_paths)
        self.ui.add_paths_btn2.clicked.connect(self.select_backup_paths)
        self.ui.path_list.doubleClicked.connect(self.select_backup_paths)
        self.ui.path_list2.doubleClicked.connect(self.select_backup_paths)
        self.ui.compress_checkbox.checkStateChanged.connect(
            partial(
                self.set_compress_extention,
                self.ui.backup_filename,
                # Сюда прилетает эвент
            )
        )
        self.ui.compress_checkbox_2.checkStateChanged.connect(
            partial(
                self.set_compress_extention,
                self.ui.def_name_input,
                # Сюда прилетает эвент
            )
        )

        deligate = QItemDelegate(self)
        deligate.closeEditor.connect(self.rename_backup)
        self.ui.backups_table.setItemDelegate(deligate)

        self.auto_backup = AutoBackup(self.config_manager)
        self.auto_backup.save_baskup_signal.connect(self.save_auto_backup)

        self.restore_config()
        self.update_table()
        self.ui.backups_table.resizeColumnsToContents()

    def restore_backup(self, backup_path: str):
        RestoreDialog(backup_path)

    def save_auto_backup(self, backup_path: str, backup_name: str):
        """
        Сохраняет автоматическую копию с указанными путем и именем.

        Параметры:
            backup_path (str): Путь для сохранения копии.
            backup_name (str): Имя файла копии.

        Возвращает:
            None
        """
        self.config_manager.add_backup(
            backup_name, backup_path, datetime.now().isoformat(), getsize(backup_path)
        )
        self.update_table()

    def rename_backup(self, text: QLineEdit):
        """
        Переименовывает файл резервной копии, обновляет конфигурацию,
        если файл не существует.

        :param text: объект QLineEdit
        """
        item = self.ui.backups_table.selectedItems()[0]
        row = item.row()
        path = Path(item.toolTip())
        try:
            new_path = path.parent / text.text()
            path.rename(new_path)
            item.setToolTip(str(new_path))
            self.config_manager.rename_backup(row, new_path)
        except FileNotFoundError as err:
            print(err)

            self.config_manager.remove_backup(row)
            self.ui.backups_table.removeRow(item.row())
        print("Renamed:", path.parent / text.text())

    def restore_config(self) -> None:
        """
        Восстанавливает настройки конфигурации для элементов
        интерфейса пользователя, используя значения из конфига.
        Параметры и возвращаемые типы отсутствуют.
        """
        self.ui.path_input.setText(self.config_manager.def_path)
        self.ui.def_path_input.setText(self.config_manager.def_path)
        print("setting def name", self.config_manager.def_name)
        def_name = self.config_manager.def_name
        self.ui.def_name_input.setText(def_name)
        # self.ui.def_name_input.repaint()
        # self.ui.def_name_input.text()
        self.ui.backup_filename.setText(def_name)
        self.ui.interval_combo.setCurrentIndex(self.config_manager.interval)
        self.ui.autobackup_check.setChecked(self.config_manager.autobackup)
        self.ui.compress_checkbox.setChecked(self.config_manager.compress)
        self.ui.compress_checkbox_2.setChecked(self.config_manager.compress)
        # self.set_compress_extention(self.ui.backup_filename, self.ui.compress_checkbox)
        # self.set_compress_extention(self.ui.def_name_input, self.ui.compress_checkbox_2)

        self.path_list = self.config_manager.get_all_paths()
        if self.path_list:
            self.ui.no_dirs_warning.hide()
            self.ui.no_dirs_warning2.hide()
            self.ui.path_list.addItems(self.path_list)
            self.ui.path_list2.addItems(self.path_list)
        else:
            self.ui.no_dirs_warning.show()
            self.ui.no_dirs_warning2.show()
        self.auto_backup.start()

    def save_config(self) -> None:
        """
        Сохраняет настройки конфигурации, включая путь по умолчанию, имя по умолчанию, индекс выбора интервала и статус автобэкапа.
        """
        if not (self.ui.def_path_input.text() and self.ui.def_name_input.text()):
            QMessageBox.critical(
                self, "Ошибка", "Введены неверные данные для сохранения конфигурации"
            )
            return
        print("Saveing config...", self.config_manager.def_name, self.ui.def_name_input.text())
        self.config_manager.def_path = self.ui.def_path_input.text()
        self.config_manager.def_name = self.ui.def_name_input.text()
        self.config_manager.interval = self.ui.interval_combo.currentIndex()
        self.config_manager.autobackup = self.ui.autobackup_check.isChecked()

    def update_table(self) -> None:
        """
        Обновляет таблицу данными из конфигурации.
        """
        print("updating table")
        self.ui.backups_table.setRowCount(self.config_manager.get_backups_count())
        for i, (filename, filepath, date, size) in enumerate(
            [i.values() for i in self.config_manager.get_backups()]
        ):
            self.add_row(
                i,
                filename,
                filepath,
                datetime.fromisoformat(date).strftime("%d.%m.%Y %H:%M"),
                human_readable.file_size(size),
            )

    def add_row(
        self, row: int, filename: str, filepath: str, date: str, size: str
    ) -> None:
        """
        Добавляет строку в таблицу резервных копий с указанными данными:
        именем файла, путем файла, датой и размером.

        :param row: Индекс строки для добавления
        :param filename: Название файла
        :param filepath: Путь к файлу
        :param date: Дата создания резервной копии
        :param size: Размер файла
        """
        # Filename
        item = QTableWidgetItem(filename)
        self.ui.backups_table.setItem(row, 0, item)
        item.setToolTip(filepath)
        # Date
        item = QTableWidgetItem(date)
        item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.ui.backups_table.setItem(row, 1, item)
        # Size
        item = QTableWidgetItem(size)
        item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.ui.backups_table.setItem(row, 2, item)
        # Restore
        button = QPushButton()
        button.clicked.connect(lambda: self.restore_backup(filepath))
        button.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_BrowserReload)
        )
        button.setToolTip("Восстановить")
        self.ui.backups_table.setCellWidget(row, 3, button)
        # Delete
        button = QPushButton()
        button.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_DialogCloseButton)
        )
        button.clicked.connect(
            lambda: self.remove_backup(self.ui.backups_table.selectedIndexes()[0].row())
        )
        button.setToolTip("Удалить")
        self.ui.backups_table.setCellWidget(row, 4, button)

    def remove_backup(self, row: int) -> None:
        """
        Удаляет запись о резервной копии из конфигурации и интерфейса
        по указанному номеру строки.

        :param row: Индекс удаляемой записи о резервной копии.
        """
        print("removing backup")
        item = self.config_manager.remove_backup(row)
        try:
            os.remove(item["filepath"])
        except FileNotFoundError:
            pass
        self.ui.backups_table.removeRow(row)

    def browse_folder(self, input: QLineEdit) -> None:
        """
        Открывает диалог выбора директории и записывает выбранный путь в QLineEdit.
        :param input: QLineEdit, куда будет установлен путь к папке.
        """
        file_path = QFileDialog.getExistingDirectory(
            self, "Выберите папку для резервных копий", os.path.expanduser("~")
        )
        if file_path:
            print(f"Selected folder: {file_path}")
            input.setText(file_path)
        else:
            print("No folder was selected.")

    def browse_file(self, input: QLineEdit) -> None:
        """
        Метод browse_file позволяет пользователю выбрать файл для сохранения.
        Принимает QLineEdit как параметр для вывода пути выбранного файла.
        """
        filepath, _ = QFileDialog.getSaveFileName(
            self, "Выберите название резервной копии", os.path.expanduser("~"), "*.tar"
        )
        if filepath:
            print(f"Selected file: {filepath}")
            input.setText(filepath)
        else:
            print("No file was selected.")

    def start_manual_backup(self) -> None:
        """
        Запускает процесс ручного бэкапа.

        Параметры отсутствуют.
        Возвращаемое значение не предусмотрено.
        """
        path = self.ui.path_input.text()
        name_tamplate = self.ui.backup_filename.text()
        if not (path and os.path.exists(path) and name_tamplate and not ()):
            QMessageBox.critical(
                self, "Ошибка", "Введены неверные данные для резервной копии!"
            )
            return
        BackupDialog(
            Path(self.ui.path_input.text())
            / datetime.now().strftime(self.ui.backup_filename.text()),
            self.path_list,
            self.config_manager,
            self.update_table,
            self.ui.compress_checkbox.isChecked(),
        )

    def set_compress_extention(
        self, input: QLineEdit, check_state: Qt.CheckState | QCheckBox
    ) -> None:
        if not self.isVisible():
            return
        text: str = input.text()

        if isinstance(check_state, QCheckBox):
            is_checked: bool = check_state.isChecked()
        else:
            is_checked: bool = check_state == Qt.CheckState.Checked

        if is_checked and not text.endswith(".gz"):
            input.setText(text + ".gz")
        else:
            input.setText(text.removesuffix(".gz"))

    def select_backup_paths(self) -> None:
        fs = FolderSelection(self.config_manager)
        paths = fs.select_paths()
        self.config_manager.set_all_paths(paths)
        self.ui.path_list.clear()
        self.ui.path_list2.clear()

        if paths:
            self.ui.no_dirs_warning.hide()
            self.ui.no_dirs_warning2.hide()
        else:
            self.ui.no_dirs_warning.show()
            self.ui.no_dirs_warning2.show()

        self.path_list = paths

        for path in paths:
            self.ui.path_list.addItem(path)
            self.ui.path_list2.addItem(path)
