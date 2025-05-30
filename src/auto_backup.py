from datetime import datetime
from PySide6.QtCore import QThread, QProcess, Signal
from config_manager import ConfigManager
from time import sleep


INTERVALS = (
    60 * 5,  # 5 minutes
    # 5,  # 5 seconds for testing
    60 * 60,  # 1 hour
    60 * 60 * 24,  # 1 day
    60 * 60 * 24 * 7,  # 1 week
)


class AutoBackup(QThread):
    save_baskup_signal = Signal(str, str)

    def __init__(self, config_manager: ConfigManager) -> None:
        """
        Инициализирует объект AutoBackup.

        Параметры:
                config_manager (ConfigManager): Объект менеджера конфигурации.

        Возвращает:
                None
        """
        super(AutoBackup, self).__init__()
        self.config_manager = config_manager
        self.finished.connect(self.__del__)

    def __del__(self):
        """
        Метод деструктора для освобождения ресурсов при удалении объекта.
        """
        print("Destroing AutoBackup thread...")
        self.terminate()

    def run(self):
        """
        Запускает процесс бэкапа в соответствии с настройками конфигурации.
        """
        while True:
            while not self.config_manager.autobackup:
                # print("Waiting...")
                sleep(1)
            print("Backuping...")
            filename = datetime.now().strftime(self.config_manager.def_name)
            filepath = self.config_manager.def_path + "/" + filename
            process = QProcess()
            process.readyReadStandardError.connect(
                lambda: print(
                    bytes(process.readAllStandardError().data()).decode().strip()
                )
            )
            process.readyReadStandardOutput.connect(
                lambda: print(
                    bytes(process.readAllStandardOutput().data()).decode().strip()
                )
            )
            process.start(
                "tar",
                [
                    "cvzf" if self.config_manager.compress else "cvf",
                    filepath,
                    *self.config_manager.get_all_paths(),
                ],
            )
            print(process.waitForFinished(2147483647))
            self.save_baskup_signal.emit(filepath, filename)
            print(
                "Sleeping",
                INTERVALS[self.config_manager.interval],
                "second(s)",
            )
            sleep(INTERVALS[self.config_manager.interval])
