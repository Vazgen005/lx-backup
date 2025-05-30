# type: ignore
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 378)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 250))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon(QIcon.fromTheme(u"system-reboot"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.backup_tab = QWidget()
        self.backup_tab.setObjectName(u"backup_tab")
        self.verticalLayout_6 = QVBoxLayout(self.backup_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.path_label = QLabel(self.backup_tab)
        self.path_label.setObjectName(u"path_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.path_label.sizePolicy().hasHeightForWidth())
        self.path_label.setSizePolicy(sizePolicy1)
        self.path_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_6.addWidget(self.path_label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.path_input = QLineEdit(self.backup_tab)
        self.path_input.setObjectName(u"path_input")

        self.horizontalLayout_5.addWidget(self.path_input)

        self.path_button = QPushButton(self.backup_tab)
        self.path_button.setObjectName(u"path_button")

        self.horizontalLayout_5.addWidget(self.path_button)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.label_2 = QLabel(self.backup_tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.backup_filename = QLineEdit(self.backup_tab)
        self.backup_filename.setObjectName(u"backup_filename")

        self.verticalLayout_6.addWidget(self.backup_filename)

        self.compress_checkbox = QCheckBox(self.backup_tab)
        self.compress_checkbox.setObjectName(u"compress_checkbox")
        self.compress_checkbox.setChecked(True)

        self.verticalLayout_6.addWidget(self.compress_checkbox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.backup_tab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.add_paths_btn = QPushButton(self.backup_tab)
        self.add_paths_btn.setObjectName(u"add_paths_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.add_paths_btn.sizePolicy().hasHeightForWidth())
        self.add_paths_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.add_paths_btn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.no_dirs_warning = QLabel(self.backup_tab)
        self.no_dirs_warning.setObjectName(u"no_dirs_warning")
        sizePolicy1.setHeightForWidth(self.no_dirs_warning.sizePolicy().hasHeightForWidth())
        self.no_dirs_warning.setSizePolicy(sizePolicy1)
        self.no_dirs_warning.setVisible(False)
        self.no_dirs_warning.setStyleSheet(u"color: red")

        self.verticalLayout_6.addWidget(self.no_dirs_warning)

        self.path_list = QListWidget(self.backup_tab)
        self.path_list.setObjectName(u"path_list")
        self.path_list.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_6.addWidget(self.path_list)

        self.line = QFrame(self.backup_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.backup_btn = QPushButton(self.backup_tab)
        self.backup_btn.setObjectName(u"backup_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.backup_btn.sizePolicy().hasHeightForWidth())
        self.backup_btn.setSizePolicy(sizePolicy3)

        self.verticalLayout_6.addWidget(self.backup_btn)

        self.tabs.addTab(self.backup_tab, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.verticalLayout = QVBoxLayout(self.settings_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.warning_label = QLabel(self.settings_tab)
        self.warning_label.setObjectName(u"warning_label")
        self.warning_label.setStyleSheet(u"color: red")

        self.verticalLayout.addWidget(self.warning_label)

        self.def_path_label = QLabel(self.settings_tab)
        self.def_path_label.setObjectName(u"def_path_label")
        sizePolicy1.setHeightForWidth(self.def_path_label.sizePolicy().hasHeightForWidth())
        self.def_path_label.setSizePolicy(sizePolicy1)
        self.def_path_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.def_path_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.def_path_input = QLineEdit(self.settings_tab)
        self.def_path_input.setObjectName(u"def_path_input")

        self.horizontalLayout_3.addWidget(self.def_path_input)

        self.def_path_button = QPushButton(self.settings_tab)
        self.def_path_button.setObjectName(u"def_path_button")

        self.horizontalLayout_3.addWidget(self.def_path_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.def_name_label = QLabel(self.settings_tab)
        self.def_name_label.setObjectName(u"def_name_label")
        sizePolicy1.setHeightForWidth(self.def_name_label.sizePolicy().hasHeightForWidth())
        self.def_name_label.setSizePolicy(sizePolicy1)
        self.def_name_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.def_name_label)

        self.def_name_input = QLineEdit(self.settings_tab)
        self.def_name_input.setObjectName(u"def_name_input")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.def_name_input.sizePolicy().hasHeightForWidth())
        self.def_name_input.setSizePolicy(sizePolicy4)
        self.def_name_input.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.def_name_input)

        self.interval_label = QLabel(self.settings_tab)
        self.interval_label.setObjectName(u"interval_label")
        self.interval_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.interval_label)

        self.interval_combo = QComboBox(self.settings_tab)
        self.interval_combo.addItem("")
        self.interval_combo.addItem("")
        self.interval_combo.addItem("")
        self.interval_combo.addItem("")
        self.interval_combo.setObjectName(u"interval_combo")

        self.verticalLayout.addWidget(self.interval_combo)

        self.compress_checkbox_2 = QCheckBox(self.settings_tab)
        self.compress_checkbox_2.setObjectName(u"compress_checkbox_2")

        self.verticalLayout.addWidget(self.compress_checkbox_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.settings_tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.add_paths_btn2 = QPushButton(self.settings_tab)
        self.add_paths_btn2.setObjectName(u"add_paths_btn2")

        self.horizontalLayout_4.addWidget(self.add_paths_btn2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.no_dirs_warning2 = QLabel(self.settings_tab)
        self.no_dirs_warning2.setObjectName(u"no_dirs_warning2")
        self.no_dirs_warning2.setStyleSheet(u"color: red")

        self.verticalLayout.addWidget(self.no_dirs_warning2)

        self.path_list2 = QListWidget(self.settings_tab)
        self.path_list2.setObjectName(u"path_list2")
        self.path_list2.setStyleSheet(u"background-color: transparent")

        self.verticalLayout.addWidget(self.path_list2)

        self.line_2 = QFrame(self.settings_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.autobackup_check = QCheckBox(self.settings_tab)
        self.autobackup_check.setObjectName(u"autobackup_check")

        self.horizontalLayout.addWidget(self.autobackup_check)

        self.save_autobackup_settings_btn = QPushButton(self.settings_tab)
        self.save_autobackup_settings_btn.setObjectName(u"save_autobackup_settings_btn")

        self.horizontalLayout.addWidget(self.save_autobackup_settings_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabs.addTab(self.settings_tab, "")
        self.backup_list_tab = QWidget()
        self.backup_list_tab.setObjectName(u"backup_list_tab")
        self.verticalLayout_3 = QVBoxLayout(self.backup_list_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.backups_table = QTableWidget(self.backup_list_tab)
        if (self.backups_table.columnCount() < 5):
            self.backups_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.backups_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.backups_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.backups_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.backups_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.backups_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.backups_table.setObjectName(u"backups_table")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.backups_table.sizePolicy().hasHeightForWidth())
        self.backups_table.setSizePolicy(sizePolicy6)
        self.backups_table.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.backups_table.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.backups_table.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.backups_table.setRowCount(0)
        self.backups_table.setColumnCount(5)
        self.backups_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.backups_table)

        self.backups_list_update_btn = QPushButton(self.backup_list_tab)
        self.backups_list_update_btn.setObjectName(u"backups_list_update_btn")

        self.verticalLayout_3.addWidget(self.backups_list_update_btn)

        self.tabs.addTab(self.backup_list_tab, "")
        self.info_tab = QWidget()
        self.info_tab.setObjectName(u"info_tab")
        self.verticalLayout_4 = QVBoxLayout(self.info_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.info_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 765, 906))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_5.addWidget(self.label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.tabs.addTab(self.info_tab, "")

        self.verticalLayout_2.addWidget(self.tabs)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.autobackup_check.toggled.connect(self.warning_label.setHidden)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u041e\u0421\u0410 \u043a\u043e\u043f\u0438\u044f", None))
        self.path_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044f \u0434\u043b\u044f \u043a\u043e\u043f\u0438\u0438", None))
        self.path_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043a\u043e\u043f\u0438\u0438", None))
        self.backup_filename.setText(QCoreApplication.translate("MainWindow", u"backup-%d.%m.%Y-%H:%M:%S.tar", None))
        self.compress_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0436\u0430\u0442\u044c \u043a\u043e\u043f\u0438\u044e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u0443\u0435\u043c\u044b\u0435 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u0438", None))
        self.add_paths_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.no_dirs_warning.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435! \u041d\u0438 \u043e\u0434\u043d\u043e\u0439 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u0438 \u043d\u0435 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u043e!", None))
        self.backup_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0427\u0410\u0422\u042c", None))
        self.tabs.setTabText(self.tabs.indexOf(self.backup_tab), QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u0430\u044f \u043a\u043e\u043f\u0438\u044f", None))
        self.warning_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435! \u0410\u0432\u0442\u043e \u043a\u043e\u043f\u0438\u044f \u043d\u0435 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0430!", None))
        self.def_path_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044f \u0434\u043b\u044f \u043a\u043e\u043f\u0438\u0439", None))
        self.def_path_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.def_name_label.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043a\u043e\u043f\u0438\u0439 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.def_name_input.setText(QCoreApplication.translate("MainWindow", u"backup-%d.%m.%Y-%H:%M:%S.tar", None))
        self.interval_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u0430\u0432\u0442\u043e \u043a\u043e\u043f\u0438\u0438", None))
        self.interval_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"5 \u043c\u0438\u043d\u0443\u0442", None))
        self.interval_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"1 \u0447\u0430\u0441", None))
        self.interval_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"1 \u0434\u0435\u043d\u044c", None))
        self.interval_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"1 \u043d\u0435\u0434\u0435\u043b\u044f", None))

        self.compress_checkbox_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0436\u0438\u043c\u0430\u0442\u044c \u043a\u043e\u043f\u0438\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u0443\u0435\u043c\u044b\u0435 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u0438", None))
        self.add_paths_btn2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.no_dirs_warning2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435! \u041d\u0438 \u043e\u0434\u043d\u043e\u0439 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u0438 \u043d\u0435 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u043e!", None))
        self.autobackup_check.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0410\u0432\u0442\u043e \u043a\u043e\u043f\u0438\u044e", None))
        self.save_autobackup_settings_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.tabs.setTabText(self.tabs.indexOf(self.settings_tab), QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e \u043a\u043e\u043f\u0438\u044f", None))
        ___qtablewidgetitem = self.backups_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.backups_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem2 = self.backups_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0441", None));
        self.backups_list_update_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.tabs.setTabText(self.tabs.indexOf(self.backup_list_tab), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043a\u043e\u043f\u0438\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">1. \u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0439 \u043a\u043e\u043f\u0438\u0438 \u0432\u0440\u0443\u0447\u043d\u0443\u044e</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','R"
                        "oboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u041e\u0442\u043a\u0440\u043e\u0439\u0442\u0435 \u0432\u043a\u043b\u0430\u0434\u043a\u0443 &quot;\u0420\u0443\u0447\u043d\u0430\u044f \u043a\u043e\u043f\u0438\u044f&quot;</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044e \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0439 \u043a\u043e\u043f\u0438\u0438 (\u043a\u043d\u043e\u043f\u043a\u0430 &quot;\u041e\u0431\u0437\u043e\u0440&quot;)</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch'"
                        ",'Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u041f\u0440\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u0438 \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043a\u043e\u043f\u0438\u0438</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435, \u043d\u0443\u0436\u043d\u043e \u043b\u0438 \u0441\u0436\u0438\u043c\u0430\u0442\u044c \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u0443\u044e \u043a\u043e\u043f\u0438\u044e (\u0433\u0430\u043b\u043e\u0447"
                        "\u043a\u0430 &quot;\u0421\u0436\u0430\u0442\u044c \u043a\u043e\u043f\u0438\u044e&quot;)</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u0414\u043e\u0431\u0430\u0432\u044c\u0442\u0435 \u043f\u0430\u043f\u043a\u0438 \u0434\u043b\u044f \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0433\u043e \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f (\u043a\u043d\u043e\u043f\u043a\u0430 &quot;\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c&quot;)</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u041d\u0430\u0436\u043c\u0438\u0442\u0435"
                        " \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u041d\u0410\u0427\u0410\u0422\u042c&quot; \u0434\u043b\u044f \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">2. \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0433\u043e \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-col"
                        "or:#292a2d;\">    \u041e\u0442\u043a\u0440\u043e\u0439\u0442\u0435 \u0432\u043a\u043b\u0430\u0434\u043a\u0443 &quot;\u0410\u0432\u0442\u043e \u043a\u043e\u043f\u0438\u044f&quot;</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044e \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043a\u043e\u043f\u0438\u0439</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; backgro"
                        "und-color:#292a2d;\">    \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043a\u043e\u043f\u0438\u0439</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043a\u043e\u043f\u0438\u0439 \u0438\u0437 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f"
                        "8faff; background-color:#292a2d;\">    \u0423\u043a\u0430\u0436\u0438\u0442\u0435, \u043d\u0443\u0436\u043d\u043e \u043b\u0438 \u0441\u0436\u0438\u043c\u0430\u0442\u044c \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043a\u043e\u043f\u0438\u0438</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u0414\u043e\u0431\u0430\u0432\u044c\u0442\u0435 \u043f\u0430\u043f\u043a\u0438 \u0434\u043b\u044f \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0433\u043e \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; fon"
                        "t-size:16px; color:#f8faff; background-color:#292a2d;\">    \u0412\u043a\u043b\u044e\u0447\u0438\u0442\u0435 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 (\u0433\u0430\u043b\u043e\u0447\u043a\u0430 &quot;\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0410\u0432\u0442\u043e \u043a\u043e\u043f\u0438\u044e&quot;)</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u041d\u0430\u0436\u043c\u0438\u0442\u0435 &quot;\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438&quot;</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','"
                        "Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">3. \u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u043c\u0438 \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u044b\u043c\u0438 \u043a\u043e\u043f\u0438\u044f\u043c\u0438</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u041e\u0442\u043a\u0440\u043e\u0439\u0442\u0435 \u0432\u043a\u043b\u0430\u0434\u043a\u0443 &quot;\u0412\u0441\u0435 \u043a\u043e\u043f\u0438\u0438&quot;</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; f"
                        "ont-size:16px; color:#f8faff; background-color:#292a2d;\">    \u0414\u043b\u044f \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u0437 \u043a\u043e\u043f\u0438\u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \u0441 \u0438\u043a\u043e\u043d\u043a\u043e\u0439 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u0439 \u0441\u0442\u0440\u043e\u043a\u0435</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u0414\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0439 \u043a\u043e\u043f\u0438\u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a"
                        "\u043d\u043e\u043f\u043a\u0443 \u0441 \u043a\u0440\u0435\u0441\u0442\u0438\u043a\u043e\u043c \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u0439 \u0441\u0442\u0440\u043e\u043a\u0435</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u0414\u043b\u044f \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u043f\u0438\u0441\u043a\u0430 \u043a\u043e\u043f\u0438\u0439 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c&quot;</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif';"
                        " font-size:16px; color:#f8faff; background-color:#292a2d;\">4. \u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0437 \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0439 \u043a\u043e\u043f\u0438\u0438</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u041e\u0442\u043a\u0440\u043e\u0439\u0442\u0435 \u0432\u043a\u043b\u0430\u0434\u043a\u0443 &quot;\u0412\u0441\u0435 \u043a\u043e\u043f\u0438\u0438&quot;</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u041d\u0430\u0439\u0434\u0438\u0442\u0435 \u043d\u0443"
                        "\u0436\u043d\u0443\u044e \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u0443\u044e \u043a\u043e\u043f\u0438\u044e \u0432 \u0441\u043f\u0438\u0441\u043a\u0435</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; background-color:#292a2d;\">    \u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \u0441 \u0438\u043a\u043e\u043d\u043a\u043e\u0439 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u0439 \u0441\u0442\u0440\u043e\u043a\u0435</span></p><p><span style=\" font-family:'DeepSeek-CJK-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Noto Sans','Ubuntu','Cantarell','Helvetica Neue','Oxygen','Open Sans','sans-serif'; font-size:16px; color:#f8faff; back"
                        "ground-color:#292a2d;\">    \u0414\u043e\u0436\u0434\u0438\u0442\u0435\u0441\u044c \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0430 \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f</span></p></body></html>", None))
        self.tabs.setTabText(self.tabs.indexOf(self.info_tab), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

