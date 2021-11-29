# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUImain.ui'
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
        MainWindow.resize(1100, 798)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen_2 = QAction(MainWindow)
        self.actionOpen_2.setObjectName(u"actionOpen_2")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.GB_foreseen = QGroupBox(self.centralwidget)
        self.GB_foreseen.setObjectName(u"GB_foreseen")
        self.GB_foreseen.setGeometry(QRect(10, 10, 381, 471))
        font = QFont()
        font.setPointSize(12)
        self.GB_foreseen.setFont(font)
        self.layoutWidget = QWidget(self.GB_foreseen)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 25, 356, 408))
        self.LT_foreseen = QGridLayout(self.layoutWidget)
        self.LT_foreseen.setObjectName(u"LT_foreseen")
        self.LT_foreseen.setContentsMargins(0, 0, 0, 0)
        self.LT_input = QGridLayout()
        self.LT_input.setObjectName(u"LT_input")
        self.LE_cyl_dm = QLineEdit(self.layoutWidget)
        self.LE_cyl_dm.setObjectName(u"LE_cyl_dm")
        font1 = QFont()
        font1.setPointSize(10)
        self.LE_cyl_dm.setFont(font1)

        self.LT_input.addWidget(self.LE_cyl_dm, 3, 1, 1, 1)

        self.label_piston_jour = QLabel(self.layoutWidget)
        self.label_piston_jour.setObjectName(u"label_piston_jour")
        self.label_piston_jour.setFont(font1)

        self.LT_input.addWidget(self.label_piston_jour, 2, 0, 1, 1)

        self.LE_comp_rat = QLineEdit(self.layoutWidget)
        self.LE_comp_rat.setObjectName(u"LE_comp_rat")
        self.LE_comp_rat.setFont(font1)

        self.LT_input.addWidget(self.LE_comp_rat, 1, 1, 1, 1)

        self.label_rod_len = QLabel(self.layoutWidget)
        self.label_rod_len.setObjectName(u"label_rod_len")
        self.label_rod_len.setFont(font1)

        self.LT_input.addWidget(self.label_rod_len, 4, 0, 1, 1)

        self.LE_xup_cor = QLineEdit(self.layoutWidget)
        self.LE_xup_cor.setObjectName(u"LE_xup_cor")
        self.LE_xup_cor.setFont(font1)

        self.LT_input.addWidget(self.LE_xup_cor, 5, 1, 1, 1)

        self.label_air_press = QLabel(self.layoutWidget)
        self.label_air_press.setObjectName(u"label_air_press")
        self.label_air_press.setFont(font1)

        self.LT_input.addWidget(self.label_air_press, 6, 0, 1, 1)

        self.LE_air_press = QLineEdit(self.layoutWidget)
        self.LE_air_press.setObjectName(u"LE_air_press")
        self.LE_air_press.setFont(font1)

        self.LT_input.addWidget(self.LE_air_press, 6, 1, 1, 1)

        self.label_xup_cor = QLabel(self.layoutWidget)
        self.label_xup_cor.setObjectName(u"label_xup_cor")
        self.label_xup_cor.setFont(font1)

        self.LT_input.addWidget(self.label_xup_cor, 5, 0, 1, 1)

        self.LE_extTem = QLineEdit(self.layoutWidget)
        self.LE_extTem.setObjectName(u"LE_extTem")
        self.LE_extTem.setFont(font1)

        self.LT_input.addWidget(self.LE_extTem, 0, 1, 1, 1)

        self.LE_rod_len = QLineEdit(self.layoutWidget)
        self.LE_rod_len.setObjectName(u"LE_rod_len")
        self.LE_rod_len.setFont(font1)

        self.LT_input.addWidget(self.LE_rod_len, 4, 1, 1, 1)

        self.label_cyl_dm = QLabel(self.layoutWidget)
        self.label_cyl_dm.setObjectName(u"label_cyl_dm")
        self.label_cyl_dm.setFont(font1)

        self.LT_input.addWidget(self.label_cyl_dm, 3, 0, 1, 1)

        self.label_comp_rat = QLabel(self.layoutWidget)
        self.label_comp_rat.setObjectName(u"label_comp_rat")
        self.label_comp_rat.setFont(font1)

        self.LT_input.addWidget(self.label_comp_rat, 1, 0, 1, 1)

        self.LE_piston_jour = QLineEdit(self.layoutWidget)
        self.LE_piston_jour.setObjectName(u"LE_piston_jour")
        self.LE_piston_jour.setFont(font1)

        self.LT_input.addWidget(self.LE_piston_jour, 2, 1, 1, 1)

        self.label_extTem = QLabel(self.layoutWidget)
        self.label_extTem.setObjectName(u"label_extTem")
        self.label_extTem.setFont(font1)

        self.LT_input.addWidget(self.label_extTem, 0, 0, 1, 1)


        self.LT_foreseen.addLayout(self.LT_input, 0, 0, 1, 2)

        self.BT_math = QPushButton(self.layoutWidget)
        self.BT_math.setObjectName(u"BT_math")
        font2 = QFont()
        font2.setPointSize(8)
        self.BT_math.setFont(font2)

        self.LT_foreseen.addWidget(self.BT_math, 1, 0, 1, 1)

        self.BT_clear = QPushButton(self.layoutWidget)
        self.BT_clear.setObjectName(u"BT_clear")
        self.BT_clear.setFont(font2)

        self.LT_foreseen.addWidget(self.BT_clear, 1, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_Compression = QLabel(self.layoutWidget)
        self.label_Compression.setObjectName(u"label_Compression")
        self.label_Compression.setFont(font1)

        self.gridLayout_4.addWidget(self.label_Compression, 0, 0, 1, 1)

        self.LE_Compression = QLineEdit(self.layoutWidget)
        self.LE_Compression.setObjectName(u"LE_Compression")
        self.LE_Compression.setFont(font1)
        self.LE_Compression.setReadOnly(True)

        self.gridLayout_4.addWidget(self.LE_Compression, 0, 1, 1, 1)

        self.label_Comp_temp_C = QLabel(self.layoutWidget)
        self.label_Comp_temp_C.setObjectName(u"label_Comp_temp_C")
        self.label_Comp_temp_C.setFont(font1)

        self.gridLayout_4.addWidget(self.label_Comp_temp_C, 1, 0, 1, 1)

        self.LE_Comp_temp_C = QLineEdit(self.layoutWidget)
        self.LE_Comp_temp_C.setObjectName(u"LE_Comp_temp_C")
        self.LE_Comp_temp_C.setFont(font1)
        self.LE_Comp_temp_C.setReadOnly(True)

        self.gridLayout_4.addWidget(self.LE_Comp_temp_C, 1, 1, 1, 1)

        self.label_Comp_temp_F = QLabel(self.layoutWidget)
        self.label_Comp_temp_F.setObjectName(u"label_Comp_temp_F")
        self.label_Comp_temp_F.setFont(font1)

        self.gridLayout_4.addWidget(self.label_Comp_temp_F, 2, 0, 1, 1)

        self.LE_Comp_temp_F = QLineEdit(self.layoutWidget)
        self.LE_Comp_temp_F.setObjectName(u"LE_Comp_temp_F")
        self.LE_Comp_temp_F.setFont(font1)
        self.LE_Comp_temp_F.setReadOnly(True)

        self.gridLayout_4.addWidget(self.LE_Comp_temp_F, 2, 1, 1, 1)

        self.label_watt = QLabel(self.layoutWidget)
        self.label_watt.setObjectName(u"label_watt")
        self.label_watt.setFont(font1)

        self.gridLayout_4.addWidget(self.label_watt, 3, 0, 1, 1)

        self.LE_watt = QLineEdit(self.layoutWidget)
        self.LE_watt.setObjectName(u"LE_watt")
        self.LE_watt.setFont(font1)
        self.LE_watt.setReadOnly(True)

        self.gridLayout_4.addWidget(self.LE_watt, 3, 1, 1, 1)


        self.LT_foreseen.addLayout(self.gridLayout_4, 2, 0, 1, 2)

        self.GB_data = QGroupBox(self.centralwidget)
        self.GB_data.setObjectName(u"GB_data")
        self.GB_data.setGeometry(QRect(10, 490, 381, 261))
        self.GB_data.setFont(font)
        self.label_time = QLabel(self.GB_data)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(30, 40, 128, 24))
        self.label_time.setFont(font1)
        self.label_xylanh2 = QLabel(self.GB_data)
        self.label_xylanh2.setObjectName(u"label_xylanh2")
        self.label_xylanh2.setGeometry(QRect(30, 142, 87, 21))
        self.label_xylanh2.setFont(font1)
        self.PB_xylanh4 = QProgressBar(self.GB_data)
        self.PB_xylanh4.setObjectName(u"PB_xylanh4")
        self.PB_xylanh4.setGeometry(QRect(140, 222, 118, 23))
        self.PB_xylanh4.setValue(0)
        self.label_xylanh1 = QLabel(self.GB_data)
        self.label_xylanh1.setObjectName(u"label_xylanh1")
        self.label_xylanh1.setGeometry(QRect(30, 105, 87, 21))
        self.label_xylanh1.setFont(font1)
        self.PB_xylanh1 = QProgressBar(self.GB_data)
        self.PB_xylanh1.setObjectName(u"PB_xylanh1")
        self.PB_xylanh1.setGeometry(QRect(140, 102, 118, 23))
        self.PB_xylanh1.setValue(0)
        self.PB_xylanh3 = QProgressBar(self.GB_data)
        self.PB_xylanh3.setObjectName(u"PB_xylanh3")
        self.PB_xylanh3.setGeometry(QRect(140, 182, 118, 23))
        self.PB_xylanh3.setValue(0)
        self.BT_measure_xylanh2 = QPushButton(self.GB_data)
        self.BT_measure_xylanh2.setObjectName(u"BT_measure_xylanh2")
        self.BT_measure_xylanh2.setGeometry(QRect(280, 142, 93, 28))
        self.BT_measure_xylanh2.setFont(font2)
        self.label_xylanh4 = QLabel(self.GB_data)
        self.label_xylanh4.setObjectName(u"label_xylanh4")
        self.label_xylanh4.setGeometry(QRect(30, 216, 87, 21))
        self.label_xylanh4.setFont(font1)
        self.BT_measure_xylanh3 = QPushButton(self.GB_data)
        self.BT_measure_xylanh3.setObjectName(u"BT_measure_xylanh3")
        self.BT_measure_xylanh3.setGeometry(QRect(280, 182, 93, 28))
        self.BT_measure_xylanh3.setFont(font2)
        self.label_s = QLabel(self.GB_data)
        self.label_s.setObjectName(u"label_s")
        self.label_s.setGeometry(QRect(250, 40, 31, 24))
        self.label_s.setFont(font1)
        self.PB_xylanh2 = QProgressBar(self.GB_data)
        self.PB_xylanh2.setObjectName(u"PB_xylanh2")
        self.PB_xylanh2.setGeometry(QRect(140, 142, 118, 23))
        self.PB_xylanh2.setValue(0)
        self.label_xylanh3 = QLabel(self.GB_data)
        self.label_xylanh3.setObjectName(u"label_xylanh3")
        self.label_xylanh3.setGeometry(QRect(30, 179, 87, 21))
        self.label_xylanh3.setFont(font1)
        self.BT_measure_xylanh1 = QPushButton(self.GB_data)
        self.BT_measure_xylanh1.setObjectName(u"BT_measure_xylanh1")
        self.BT_measure_xylanh1.setGeometry(QRect(280, 102, 93, 28))
        self.BT_measure_xylanh1.setFont(font2)
        self.DSB_time = QDoubleSpinBox(self.GB_data)
        self.DSB_time.setObjectName(u"DSB_time")
        self.DSB_time.setGeometry(QRect(164, 40, 80, 24))
        self.DSB_time.setFont(font2)
        self.BT_measure_xylanh4 = QPushButton(self.GB_data)
        self.BT_measure_xylanh4.setObjectName(u"BT_measure_xylanh4")
        self.BT_measure_xylanh4.setGeometry(QRect(280, 220, 93, 28))
        self.BT_measure_xylanh4.setFont(font2)
        self.GB_Table = QGroupBox(self.centralwidget)
        self.GB_Table.setObjectName(u"GB_Table")
        self.GB_Table.setGeometry(QRect(400, 20, 691, 311))
        self.GB_Table.setFont(font)
        self.TW_table = QTableWidget(self.GB_Table)
        self.TW_table.setObjectName(u"TW_table")
        self.TW_table.setGeometry(QRect(10, 30, 681, 271))
        self.BT_cancel = QPushButton(self.centralwidget)
        self.BT_cancel.setObjectName(u"BT_cancel")
        self.BT_cancel.setGeometry(QRect(760, 710, 93, 28))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.BT_cancel.setFont(font3)
        self.BT_confirm = QPushButton(self.centralwidget)
        self.BT_confirm.setObjectName(u"BT_confirm")
        self.BT_confirm.setGeometry(QRect(660, 710, 93, 28))
        self.BT_confirm.setFont(font3)
        self.GB_diagnose = QGroupBox(self.centralwidget)
        self.GB_diagnose.setObjectName(u"GB_diagnose")
        self.GB_diagnose.setGeometry(QRect(400, 330, 691, 381))
        self.GB_diagnose.setFont(font)
        self.grap_xylanh = QTabWidget(self.GB_diagnose)
        self.grap_xylanh.setObjectName(u"grap_xylanh")
        self.grap_xylanh.setGeometry(QRect(20, 30, 661, 321))
        self.grap_xylanh.setFont(font1)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.grap_xylanh1 = QGraphicsView(self.tab_1)
        self.grap_xylanh1.setObjectName(u"grap_xylanh1")
        self.grap_xylanh1.setGeometry(QRect(0, 10, 641, 301))
        self.grap_xylanh.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.grap_xylanh2 = QGraphicsView(self.tab_2)
        self.grap_xylanh2.setObjectName(u"grap_xylanh2")
        self.grap_xylanh2.setGeometry(QRect(0, 10, 651, 271))
        self.grap_xylanh.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.grap_xylanh3 = QGraphicsView(self.tab_3)
        self.grap_xylanh3.setObjectName(u"grap_xylanh3")
        self.grap_xylanh3.setGeometry(QRect(0, 10, 651, 271))
        self.grap_xylanh.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.grap_xylanh4 = QGraphicsView(self.tab_4)
        self.grap_xylanh4.setObjectName(u"grap_xylanh4")
        self.grap_xylanh4.setGeometry(QRect(0, 10, 651, 271))
        self.grap_xylanh.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 26))
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuEdit.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionOpen_2)
        self.menuEdit.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionSave_as)

        self.retranslateUi(MainWindow)

        self.grap_xylanh.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.GB_foreseen.setTitle(QCoreApplication.translate("MainWindow", u"S\u1ed1 li\u1ec7u", None))
        self.LE_cyl_dm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp s\u1ed1 li\u1ec7u", None))
        self.label_piston_jour.setText(QCoreApplication.translate("MainWindow", u"H\u00e0nh tr\u00ecnh piston", None))
        self.LE_comp_rat.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp s\u1ed1 li\u1ec7u", None))
        self.label_rod_len.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u d\u00e0i thanh truy\u1ec1n", None))
        self.LE_xup_cor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp s\u1ed1 li\u1ec7u", None))
        self.label_air_press.setText(QCoreApplication.translate("MainWindow", u"\u00c1p su\u1ea5t kh\u00ed n\u1ea1p", None))
        self.LE_air_press.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp s\u1ed1 li\u1ec7u", None))
        self.label_xup_cor.setText(QCoreApplication.translate("MainWindow", u"G\u00f3c \u0111\u00f3ng mu\u1ed9n xuppap", None))
        self.LE_extTem.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp s\u1ed1 li\u1ec7u", None))
        self.LE_rod_len.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp s\u1ed1 li\u1ec7u", None))
        self.label_cyl_dm.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01b0\u1eddng k\u00ednh xyalnh", None))
        self.label_comp_rat.setText(QCoreApplication.translate("MainWindow", u"T\u1ef7 s\u1ed1 n\u00e9n", None))
        self.LE_piston_jour.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp s\u1ed1 li\u1ec7u", None))
        self.label_extTem.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9", None))
        self.BT_math.setText(QCoreApplication.translate("MainWindow", u"T\u00ednh to\u00e1n", None))
        self.BT_clear.setText(QCoreApplication.translate("MainWindow", u"H\u1ee7y b\u1ecf", None))
        self.label_Compression.setText(QCoreApplication.translate("MainWindow", u"\u00c1p su\u1ea5t n\u00e9n", None))
        self.LE_Compression.setPlaceholderText("")
        self.label_Comp_temp_C.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9 (\u0111\u1ed9 C)", None))
        self.LE_Comp_temp_C.setPlaceholderText("")
        self.label_Comp_temp_F.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9 (\u0111\u1ed9 F)", None))
        self.LE_Comp_temp_F.setPlaceholderText("")
        self.label_watt.setText(QCoreApplication.translate("MainWindow", u"C\u00f4ng n\u00e9n", None))
        self.LE_watt.setPlaceholderText("")
        self.GB_data.setTitle(QCoreApplication.translate("MainWindow", u"D\u1eef li\u1ec7u", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian \u0111o", None))
        self.label_xylanh2.setText(QCoreApplication.translate("MainWindow", u"\u0110o xylanh 2", None))
        self.label_xylanh1.setText(QCoreApplication.translate("MainWindow", u"\u0110o xylanh 1", None))
        self.BT_measure_xylanh2.setText(QCoreApplication.translate("MainWindow", u"X\u00e1c nh\u1eadn", None))
        self.label_xylanh4.setText(QCoreApplication.translate("MainWindow", u"\u0110o xylanh 4", None))
        self.BT_measure_xylanh3.setText(QCoreApplication.translate("MainWindow", u"X\u00e1c nh\u1eadn", None))
        self.label_s.setText(QCoreApplication.translate("MainWindow", u"(s)", None))
        self.label_xylanh3.setText(QCoreApplication.translate("MainWindow", u"\u0110o xylanh 3", None))
        self.BT_measure_xylanh1.setText(QCoreApplication.translate("MainWindow", u"X\u00e1c nh\u1eadn", None))
        self.BT_measure_xylanh4.setText(QCoreApplication.translate("MainWindow", u"X\u00e1c nh\u1eadn", None))
        self.GB_Table.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng s\u1ed1 li\u1ec7u", None))
        self.BT_cancel.setText(QCoreApplication.translate("MainWindow", u"Tho\u00e1t", None))
        self.BT_confirm.setText(QCoreApplication.translate("MainWindow", u"X\u00e1c nh\u1eadn", None))
        self.GB_diagnose.setTitle(QCoreApplication.translate("MainWindow", u"Ch\u1ea9n \u0111o\u00e1n", None))
        self.grap_xylanh.setTabText(self.grap_xylanh.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Xylanh 1", None))
        self.grap_xylanh.setTabText(self.grap_xylanh.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Xylanh 2", None))
        self.grap_xylanh.setTabText(self.grap_xylanh.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Xylanh 3", None))
        self.grap_xylanh.setTabText(self.grap_xylanh.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Xylanh 4", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

