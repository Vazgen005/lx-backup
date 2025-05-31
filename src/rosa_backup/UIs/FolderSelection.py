# type: ignore
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FolderSelection.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_FolderSelection(object):
    def setupUi(self, FolderSelection):
        if not FolderSelection.objectName():
            FolderSelection.setObjectName(u"FolderSelection")
        FolderSelection.resize(507, 324)
        self.verticalLayout_2 = QVBoxLayout(FolderSelection)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.path_table = QTableWidget(FolderSelection)
        if (self.path_table.columnCount() < 2):
            self.path_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.path_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.path_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.path_table.setObjectName(u"path_table")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_table.sizePolicy().hasHeightForWidth())
        self.path_table.setSizePolicy(sizePolicy)
        self.path_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.path_table)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_path_btn = QPushButton(FolderSelection)
        self.add_path_btn.setObjectName(u"add_path_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_path_btn.sizePolicy().hasHeightForWidth())
        self.add_path_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.add_path_btn)

        self.cancel_btn = QPushButton(FolderSelection)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(FolderSelection)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout.addWidget(self.save_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(FolderSelection)

        QMetaObject.connectSlotsByName(FolderSelection)
    # setupUi

    def retranslateUi(self, FolderSelection):
        FolderSelection.setWindowTitle(QCoreApplication.translate("FolderSelection", u"\u0412\u044b\u0431\u043e\u0440 \u043f\u0430\u043f\u043a\u0438", None))
        ___qtablewidgetitem = self.path_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FolderSelection", u"\u041f\u0443\u0442\u044c", None));
        ___qtablewidgetitem1 = self.path_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FolderSelection", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None));
        self.add_path_btn.setText(QCoreApplication.translate("FolderSelection", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cancel_btn.setText(QCoreApplication.translate("FolderSelection", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.save_btn.setText(QCoreApplication.translate("FolderSelection", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

