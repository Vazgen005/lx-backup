from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QProcess, QThread, Signal
from .UIs.BackupingDialog import Ui_Dialog
from pathlib import Path


class RestoreThread(QThread):
    restore_log_signal = Signal(str)

    def __init__(self, filepath: str) -> None:
        """
        Инициализирует поток восстановления.

        :param dialog: экземпляр RestoreDialog
        """
        super(RestoreThread, self).__init__()
        self.filepath = filepath

    def run(self):
        """
        Запускает процесс восстановления с использованием диалога.
        """
        process = QProcess()
        process.readyReadStandardOutput.connect(
            lambda: self.restore_log_signal.emit(
                bytes(process.readAllStandardOutput().data()).decode().strip()
            )
        )
        process.readyReadStandardError.connect(
            lambda: self.restore_log_signal.emit(
                bytes(process.readAllStandardError().data()).decode().strip()
            )
        )
        #  tar xvf "$1" -C /
        process.start("tar", ["xvf", self.filepath, "-C", "/"])
        process.waitForFinished(2147483647)


class RestoreDialog(QDialog):
    def __init__(self, filepath: str):
        """
        Инициализирует RestoreDialog с использованием указанного пути файла.

        Параметры:
                filepath (str): Путь к файлу для инициализации.

        Возвращает:
                None
        """
        super(RestoreDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Восстановление резервной копии")
        self.ui.name_text.setText(Path(filepath).name)

        self.ui.close_btn.clicked.connect(self.close)

        self.filepath = filepath

        self.restore_thread = RestoreThread(filepath)
        self.restore_thread.start()

        self.restore_thread.restore_log_signal.connect(
            lambda x: self.ui.textEdit.append(x)
        )
        self.restore_thread.finished.connect(lambda: self.on_restore_backup_finished())
        self.exec()

    def start_restore(self):
        """
        Функция start_restore инициирует процесс восстановления.
        Проверяет наличие пути к файлу в self.filepath, выводит
        сообщение об ошибке, если путь неверен, и возвращает
        управление. В случае наличия пути запускает процесс
        с использованием скрипта restore.sh и ожидает его
        завершения.
        """
        if not self.filepath:
            self.ui.close_btn.setEnabled(True)
            self.ui.textEdit.append("Выбран неверный путь")
            return
        self.restore_thread.restore_log_signal.emit(self.filepath)
        path = Path(self.filepath)
        self.ui.name_text.setText(path.name)

    def on_restore_backup_finished(self):
        """
        Обрабатывает событие завершения восстановления бэкапа.

        :param dialog: экземпляр класса RestoreDialog
        :return: None
        """
        self.ui.close_btn.setEnabled(True)
        self.ui.textEdit.append("Готово")
