from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import numpy as np
from modules.modules_math.math_analysis import *


class Ui(QtWidgets.QMainWindow):
    """
    Application
    """

    def __init__(self, main_path):
        super(Ui, self).__init__()
        self.main_path = main_path
        # load GUI
        gui_path = os.path.abspath(
            os.path.join(main_path, "GUI", "GUImain.ui"))
        uic.loadUi(gui_path, self)
        self.setup_lineEdit()
        self.setup_pushButton()
        self.setup_foreseen_children()
        self.show()

    def setup_lineEdit(self):
        LE_extTem: QLineEdit = self.findChild(QLineEdit, "LE_extTem")
        LE_comp_rat: QLineEdit = self.findChild(QLineEdit, "LE_comp_rat")
        LE_piston_jour: QLineEdit = self.findChild(QLineEdit, "LE_piston_jour")
        LE_cyl_dm: QLineEdit = self.findChild(QLineEdit, "LE_cyl_dm")
        LE_rod_len: QLineEdit = self.findChild(QLineEdit, "LE_rod_len")
        LE_xup_cor: QLineEdit = self.findChild(QLineEdit, "LE_xup_cor")
        LE_air_press: QLineEdit = self.findChild(QLineEdit, "LE_air_press")
        icon_path: str = os.path.abspath(os.path.join(
            self.main_path, "source/icon", "exclamation_mark.png"))
        icon = QIcon(icon_path)
        LE_extTem.action = LE_extTem.addAction(
            icon, LE_extTem.TrailingPosition)
        LE_comp_rat.action = LE_comp_rat.addAction(
            icon, LE_comp_rat.TrailingPosition)
        LE_piston_jour.action = LE_piston_jour.addAction(
            icon, LE_piston_jour.TrailingPosition)
        LE_cyl_dm.action = LE_cyl_dm.addAction(
            icon, LE_cyl_dm.TrailingPosition)
        LE_rod_len.action = LE_rod_len.addAction(
            icon, LE_rod_len.TrailingPosition)
        LE_xup_cor.action = LE_xup_cor.addAction(
            icon, LE_xup_cor.TrailingPosition)
        LE_air_press.action = LE_air_press.addAction(
            icon, LE_air_press.TrailingPosition)
        LE_extTem.action.setToolTip("Vui lòng nhập nhiệt độ")
        LE_comp_rat.action.setToolTip("Vui lòng nhập tỷ số nén")
        LE_cyl_dm.action.setToolTip("Vui lòng nhập hành trình piston")
        LE_piston_jour.action.setToolTip("Vui lòng nhập đường kính xi lanh")
        LE_rod_len.action.setToolTip("Vui lòng nhập chiều dài thanh truyền")
        LE_xup_cor.action.setToolTip("Vui lòng nhập góc đóng muộn Xuppap")
        LE_air_press.action.setToolTip("Vui lòng nhập áp suất khí nạp")
        LE_extTem.action.setVisible(False)
        LE_comp_rat.action.setVisible(False)
        LE_cyl_dm.action.setVisible(False)
        LE_piston_jour.action.setVisible(False)
        LE_rod_len.action.setVisible(False)
        LE_xup_cor.action.setVisible(False)
        LE_air_press.action.setVisible(False)
        LE_extTem.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_extTem,
                                                                      event=event)
        LE_comp_rat.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_comp_rat,
                                                                        event=event)
        LE_cyl_dm.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_cyl_dm,
                                                                      event=event)
        LE_piston_jour.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_piston_jour,
                                                                           event=event)
        LE_rod_len.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_rod_len,
                                                                       event=event)
        LE_xup_cor.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_xup_cor,
                                                                       event=event)
        LE_air_press.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_air_press,
                                                                         event=event)

    def LE_focusOutEvent(UI, self: QLineEdit, event: QFocusEvent):
        if self.text() == "":
            self.action.setVisible(True)
        else:
            self.action.setVisible(False)
        QLineEdit.focusOutEvent(self, event)

    def setup_pushButton(self):
        # GB_foreseen QGroupBox
        BT_math: QPushButton = self.findChild(QPushButton, "BT_math")
        BT_clear: QPushButton = self.findChild(QPushButton, "BT_clear")
        BT_math.clicked.connect(self.BT_math_click)
        BT_clear.clicked.connect(self.BT_clear_click)

    def BT_math_click(self):
        LE_extTem: QLineEdit = self.findChild(QLineEdit, "LE_extTem")
        LE_comp_rat: QLineEdit = self.findChild(QLineEdit, "LE_comp_rat")
        LE_piston_jour: QLineEdit = self.findChild(QLineEdit, "LE_piston_jour")
        LE_cyl_dm: QLineEdit = self.findChild(QLineEdit, "LE_cyl_dm")
        LE_rod_len: QLineEdit = self.findChild(QLineEdit, "LE_rod_len")
        LE_xup_cor: QLineEdit = self.findChild(QLineEdit, "LE_xup_cor")
        LE_air_press: QLineEdit = self.findChild(QLineEdit, "LE_air_press")
        math_para_lst = np.array([
            LE_extTem,
            LE_comp_rat,
            LE_piston_jour,
            LE_cyl_dm,
            LE_rod_len,
            LE_xup_cor,
            LE_air_press
        ])
        GB_foreseen: QGroupBox = self.findChild(QGroupBox, "GB_foreseen")
        if all([LE.text() != "" for LE in math_para_lst]):
            try:
                Compression_wattage, temperature_C, temperature_F, compression_pressure = caculate(extTem=float(LE_extTem.text()),
                                                                                                   comp_rat=float(LE_comp_rat.text()),
                                                                                                   piston_jour=float(LE_piston_jour.text()),
                                                                                                   cyl_dm=float(LE_cyl_dm.text()),
                                                                                                   rod_len=float(LE_rod_len.text()),
                                                                                                   xup_cor=float(LE_xup_cor.text()),
                                                                                                   air_press=float(LE_air_press.text()))
            except Exception:
                GB_foreseen.label_warning.setText("Vui lòng nhập chính xác tất cả thông số")
                GB_foreseen.label_warning.setVisible(True)
            else:
                GB_foreseen.label_warning.setVisible(False)
                LE_Compression: QLineEdit = self.findChild(QLineEdit, "LE_Compression")
                LE_Comp_temp_C: QLineEdit = self.findChild(QLineEdit, "LE_Comp_temp_C")
                LE_Comp_temp_F: QLineEdit = self.findChild(QLineEdit, "LE_Comp_temp_F")
                LE_watt: QLineEdit = self.findChild(QLineEdit, "LE_watt")
                LE_Compression.setText(str(round(Compression_wattage,4)))
                LE_Comp_temp_C.setText(str(round(temperature_C,4)))
                LE_Comp_temp_F.setText(str(round(temperature_F,4)))
                LE_watt.setText(str(round(compression_pressure,4)))
        else:
            GB_foreseen.label_warning.setVisible(True)
            for LE in math_para_lst:
                if LE.text() == "":
                    LE.action.setVisible(True)
            
            
    def setup_foreseen_children(self):
        LT_input: QGridLayout = self.findChild(QGridLayout, "LT_input")
        GB_foreseen: QGroupBox = self.findChild(QGroupBox, "GB_foreseen")
        L_Warning = QLabel(GB_foreseen)
        GB_foreseen.label_warning = L_Warning
        L_Warning.setText("Vui lòng điền đầy đủ thông tin")
        LT_input.addWidget(L_Warning,
                           8,
                           0,
                           1,
                           2,
                           Qt.AlignCenter)
        L_Warning.setStyleSheet("QLabel { color : red; }")
        L_Warning.setVisible(False)
        
    def BT_clear_click(self):
        LE_extTem: QLineEdit = self.findChild(QLineEdit, "LE_extTem")
        LE_comp_rat: QLineEdit = self.findChild(QLineEdit, "LE_comp_rat")
        LE_piston_jour: QLineEdit = self.findChild(QLineEdit, "LE_piston_jour")
        LE_cyl_dm: QLineEdit = self.findChild(QLineEdit, "LE_cyl_dm")
        LE_rod_len: QLineEdit = self.findChild(QLineEdit, "LE_rod_len")
        LE_xup_cor: QLineEdit = self.findChild(QLineEdit, "LE_xup_cor")
        LE_air_press: QLineEdit = self.findChild(QLineEdit, "LE_air_press")
        LE_extTem.action.setVisible(False)
        LE_comp_rat.action.setVisible(False)
        LE_piston_jour.action.setVisible(False)
        LE_cyl_dm.action.setVisible(False)
        LE_rod_len.action.setVisible(False)
        LE_xup_cor.action.setVisible(False)
        LE_air_press.action.setVisible(False)
        math_para_lst = np.array([
            LE_extTem.text(),
            LE_comp_rat.text(),
            LE_piston_jour.text(),
            LE_cyl_dm.text(),
            LE_rod_len.text(),
            LE_xup_cor.text(),
            LE_air_press.text()
        ])
        if any(math_para_lst != ""):
            # LE_extTem.setPlaceholderText("")
            # LE_comp_rat.setPlaceholderText("")
            # LE_piston_jour.setPlaceholderText("")
            # LE_cyl_dm.setPlaceholderText("")
            # LE_rod_len.setPlaceholderText("")
            # LE_xup_cor.setPlaceholderText("")
            # LE_air_press.setPlaceholderText("")
            LE_extTem.clear()
            LE_comp_rat.clear()
            LE_piston_jour.clear()
            LE_cyl_dm.clear()
            LE_rod_len.clear()
            LE_xup_cor.clear()
            LE_air_press.clear()


if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path)
    app.exec_()

