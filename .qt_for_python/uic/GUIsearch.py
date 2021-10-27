# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIsearch.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 350)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.GB_informatin_custom = QGroupBox(self.centralwidget)
        self.GB_informatin_custom.setObjectName(u"GB_informatin_custom")
        self.GB_informatin_custom.setGeometry(QRect(20, 10, 381, 221))
        font1 = QFont()
        font1.setPointSize(12)
        self.GB_informatin_custom.setFont(font1)
        self.label_name_custom = QLabel(self.GB_informatin_custom)
        self.label_name_custom.setObjectName(u"label_name_custom")
        self.label_name_custom.setGeometry(QRect(10, 40, 142, 41))
        self.label_name_custom.setFont(font1)
        self.label_phone_number = QLabel(self.GB_informatin_custom)
        self.label_phone_number.setObjectName(u"label_phone_number")
        self.label_phone_number.setGeometry(QRect(10, 100, 142, 31))
        self.label_phone_number.setFont(font1)
        self.label_number_car = QLabel(self.GB_informatin_custom)
        self.label_number_car.setObjectName(u"label_number_car")
        self.label_number_car.setGeometry(QRect(10, 159, 142, 31))
        self.label_number_car.setFont(font1)
        self.LE_name_custom = QLineEdit(self.GB_informatin_custom)
        self.LE_name_custom.setObjectName(u"LE_name_custom")
        self.LE_name_custom.setGeometry(QRect(160, 50, 211, 31))
        self.LE_phone_number = QLineEdit(self.GB_informatin_custom)
        self.LE_phone_number.setObjectName(u"LE_phone_number")
        self.LE_phone_number.setGeometry(QRect(160, 100, 211, 31))
        self.LE_number_car = QLineEdit(self.GB_informatin_custom)
        self.LE_number_car.setObjectName(u"LE_number_car")
        self.LE_number_car.setGeometry(QRect(160, 160, 211, 31))
        self.BT_search = QPushButton(self.centralwidget)
        self.BT_search.setObjectName(u"BT_search")
        self.BT_search.setGeometry(QRect(100, 250, 101, 31))
        self.BT_cancel = QPushButton(self.centralwidget)
        self.BT_cancel.setObjectName(u"BT_cancel")
        self.BT_cancel.setGeometry(QRect(210, 250, 111, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 26))
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuEdit.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionNew)
        self.menuEdit.addAction(self.actionSave_as)
        self.menuEdit.addAction(self.actionSave)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.GB_informatin_custom.setTitle(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin kh\u00e1ch h\u00e0ng", None))
        self.label_name_custom.setText(QCoreApplication.translate("MainWindow", u"T\u00ean kh\u00e1ch h\u00e0ng", None))
        self.label_phone_number.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.label_number_car.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3n s\u1ed1 xe", None))
        self.LE_name_custom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp t\u00ean kh\u00e1ch h\u00e0ng", None))
        self.LE_phone_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp s\u1ed1 di\u1ec7n tho\u1ea1i", None))
        self.LE_number_car.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp bi\u1ec3n s\u1ed1", None))
        self.BT_search.setText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm", None))
        self.BT_cancel.setText(QCoreApplication.translate("MainWindow", u"H\u1ee7y b\u1ecf", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

