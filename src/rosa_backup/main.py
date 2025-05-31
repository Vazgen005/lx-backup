import signal
import sys

from PySide6.QtWidgets import QApplication

from .app import App
from .config_manager import ConfigManager
from .main_window import MainWindow
from .tray_icon import TrayIcon


def handle_exit(app: QApplication, main_window: MainWindow):
    """
    Обрабатывает выход из приложения, завершает автоматическое
    сохранение и закрывает приложение.

    :param app: Экземпляр QApplication.
    :param main_window: Экземпляр MainWindow.
    """
    main_window.auto_backup.terminate()
    app.quit()


def main():
    """
    Основная функция для инициализации приложения, настройки
    главного окна и системного трея.
    """
    app = QApplication(sys.argv)
    config_manager = ConfigManager()
    main_window = MainWindow(config_manager)
    tray = TrayIcon(main_window, app)
    main_app = App(app, main_window, config_manager, tray)

    # signal.signal(signal.SIGINT, (lambda: handle_exit(app, window))())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main_app.run()


if __name__ == "__main__":
    main()
