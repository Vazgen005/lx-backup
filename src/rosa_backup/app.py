import sys
from PySide6.QtWidgets import QApplication
from .config_manager import ConfigManager

from .main_window import MainWindow
from .tray_icon import TrayIcon


class App:
    '''Главный класс приложения'''
    def __init__(
        self,
        main_app: QApplication,
        main_window: MainWindow,
        config_manager: ConfigManager,
        tray: TrayIcon,
    ) -> None:
        self.qapp: QApplication = main_app
        self.main_window: MainWindow = main_window
        self.config_manager: ConfigManager = config_manager
        self.tray: TrayIcon = tray

        main_app.setQuitOnLastWindowClosed(False)
    
    def run(self) -> None:
        '''Запустить в фоне если есть аргумент'''

        if not len(sys.argv) > 1:
            self.main_window.show()
        sys.exit(self.qapp.exec())
