# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIgraph_fix.ui'
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
        MainWindow.resize(800, 620)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.GB_grap_fix = QGroupBox(self.centralwidget)
        self.GB_grap_fix.setObjectName(u"GB_grap_fix")
        self.GB_grap_fix.setGeometry(QRect(10, 10, 781, 501))
        font = QFont()
        font.setPointSize(13)
        self.GB_grap_fix.setFont(font)
        self.GV_graph_fix = QGraphicsView(self.GB_grap_fix)
        self.GV_graph_fix.setObjectName(u"GV_graph_fix")
        self.GV_graph_fix.setGeometry(QRect(10, 30, 761, 461))
        self.BT_exit = QPushButton(self.centralwidget)
        self.BT_exit.setObjectName(u"BT_exit")
        self.BT_exit.setGeometry(QRect(340, 520, 93, 28))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.BT_exit.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuEdit.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.GB_grap_fix.setTitle(QCoreApplication.translate("MainWindow", u"H\u00ecnh \u1ea3nh xe", None))
        self.BT_exit.setText(QCoreApplication.translate("MainWindow", u"Tho\u00e1t", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

