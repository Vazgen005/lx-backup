from functools import partial
from pathlib import Path

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import (
    QDialog,
    QFileDialog,
    QPushButton,
    QStyle,
    QTableWidgetItem,
    QHeaderView
)

from config_manager import ConfigManager
from UIs.FolderSelection import Ui_FolderSelection


class FolderSelection(QDialog):
    def __init__(self, config_manager: ConfigManager):
        super(FolderSelection, self).__init__()
        self.ui = Ui_FolderSelection()
        self.ui.setupUi(self)

        self.cross = True  # True когда нажатие на крестик

        self.config_manager: ConfigManager = config_manager

        self.ui.cancel_btn.clicked.connect(self.destroy)
        self.ui.save_btn.clicked.connect(self.close)
        self.ui.add_path_btn.clicked.connect(self.add_path)

        self.ui.path_table.horizontalHeader().setSectionResizeMode(
            0,QHeaderView.ResizeMode.ResizeToContents
        )

    def close(self) -> bool:
        self.cross = False
        return super().close()

    def closeEvent(self, arg__1: QCloseEvent) -> None:
        if self.cross:
            self.destroy()
            arg__1.ignore()
        else:
            super().closeEvent(arg__1)
            self.cross = True

    def get_paths_in_table(self) -> list[str]:
        return [
            (self.ui.path_table.item(i, 0) or QTableWidgetItem()).text()
            for i in range(self.ui.path_table.rowCount())
        ]

    def rerender_table(self, paths: list[str], clear: bool = True) -> None:
        if clear:
            self.ui.path_table.clearContents()
        self.ui.path_table.setRowCount(len(paths))
        # self.ui.path_table.setColumnWidth(0, 200)
        for i, path in enumerate(paths):
            self.ui.path_table.setItem(i, 0, QTableWidgetItem(path))
            del_button = QPushButton()
            del_button.setToolTip("Удалить")
            # del_button.setMaximumWidth(20)
            del_button.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_DialogCloseButton)
            )
            del_button.clicked.connect(partial(self.remove_row, i))
            self.ui.path_table.setCellWidget(i, 1, del_button)

    def remove_row(self, row: int) -> None:
        print("removing row: ", row)
        self.ui.path_table.removeRow(row)
        self.rerender_table(self.get_paths_in_table())

    def select_paths(self) -> list[str]:
        paths = self.config_manager.get_all_paths()
        self.rerender_table(paths=paths, clear=False)

        self.exec()
        result = self.get_paths_in_table()
        self.config_manager.set_all_paths(result)
        return result

    def add_path(self) -> None:
        path = QFileDialog.getExistingDirectory(
            self, "Выбрете директорию", dir=str(Path.home())
        )
        if not path:
            return
        print(path)

        new_row_index: int = self.ui.path_table.rowCount()
        print("inserting row: ", new_row_index)
        print(new_row_index)
        self.ui.path_table.insertRow(new_row_index)
        self.ui.path_table.setItem(new_row_index, 0, QTableWidgetItem(path))
        self.rerender_table(self.get_paths_in_table())
        # self.ui.path_table.resizeColumnsToContents()
