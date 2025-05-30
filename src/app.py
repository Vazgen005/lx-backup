import sys
from PySide6.QtWidgets import QApplication
from config_manager import ConfigManager

from main_window import MainWindow
from tray_icon import TrayIcon


class App:
    def __init__(
        self,
        main_app: QApplication,
        main_window: MainWindow,
        config_manager: ConfigManager,
        tray: TrayIcon,
    ) -> None:
        self.qapp = main_app
        self.main_window = main_window
        self.config_manager = config_manager
        self.tray = tray

        main_app.setQuitOnLastWindowClosed(False)

    def run(self) -> None:
        if not len(sys.argv) > 1:
            self.main_window.show()
        sys.exit(self.qapp.exec())
