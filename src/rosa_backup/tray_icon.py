import sys
from PySide6.QtWidgets import QMessageBox, QStyle, QSystemTrayIcon, QMenu, QApplication
from PySide6.QtGui import QAction

from .main_window import MainWindow


class TrayIcon(QSystemTrayIcon):
    def __init__(self, main_window: MainWindow, app: QApplication) -> None:
        super(TrayIcon, self).__init__(
            main_window.style().standardIcon(QStyle.StandardPixmap.SP_BrowserReload),
            app,
        )

        if not QSystemTrayIcon.isSystemTrayAvailable():
            QMessageBox.critical(main_window, "Ошибка", "Системный трей недоступен.")
            sys.exit(1)

        menu = QMenu()

        self.action_exit = QAction("Выйти")
        self.action_exit.triggered.connect(
            lambda: main_window.auto_backup.finished.emit() and app.quit()
        )

        self.action_hide = QAction("Скрыть/Показать окно")
        self.action_hide.triggered.connect(
            lambda: main_window.show() if main_window.isHidden() else main_window.hide()
        )
        menu.addAction(self.action_hide)
        menu.addAction(self.action_exit)

        self.setToolTip("РОСА копия")
        self.setContextMenu(menu)
        self.show()
