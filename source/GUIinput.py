from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import numpy as np
# Import json module
from modules.library.IO_support import *
from modules.library.pyqt_support import *

class Ui(QtWidgets.QMainWindow):
    """
    Application
    """
    # Hiện chương trình
    def __init__(self, main_path):
        super(Ui, self).__init__()
        self.main_path = main_path
        # load GUI
        gui_path = os.path.abspath(
            os.path.join(main_path, "GUI", "GUIinput.ui"))
        uic.loadUi(gui_path, self)
        self.setup_lineEdit()
        self.setup_foreseen_children()
        self.setup_pushButton()
        self.show()
        
    # Điền lineEdit    
    def setup_lineEdit(self):
        LE_customer_name: QLineEdit = self.findChild(QLineEdit, "LE_customer_name")
        LE_VIN_code: QLineEdit = self.findChild(QLineEdit, "LE_VIN_code")
        LE_number_plate: QLineEdit = self.findChild(QLineEdit, "LE_number_plate")
        LE_phone_number: QLineEdit = self.findChild(QLineEdit, "LE_phone_number")
        LE_address: QLineEdit = self.findChild(QLineEdit, "LE_address")
        LE_fixing_date: QLineEdit = self.findChild(QLineEdit, "LE_fixing_date")
        icon_path: str = os.path.abspath(os.path.join(
            self.main_path, "source/icon", "exclamation_mark.png"))
        icon = QIcon(icon_path)
        
        LE_customer_name.action = LE_customer_name.addAction(
            icon, LE_customer_name.TrailingPosition)
        LE_VIN_code.action = LE_VIN_code.addAction(
            icon, LE_VIN_code.TrailingPosition)
        LE_number_plate.action = LE_number_plate.addAction(
            icon, LE_number_plate.TrailingPosition)
        LE_phone_number.action = LE_phone_number.addAction(
            icon, LE_phone_number.TrailingPosition)
        LE_address.action = LE_address.addAction(
            icon, LE_address.TrailingPosition)
        LE_fixing_date.action = LE_fixing_date.addAction(
            icon, LE_fixing_date.TrailingPosition)
        
        LE_customer_name.action.setToolTip("Vui lòng nhập tên")
        LE_VIN_code.action.setToolTip("Vui lòng nhập mã VIN (17 kí tự)")
        LE_number_plate.action.setToolTip("Vui lòng nhập biển số")
        LE_phone_number.action.setToolTip("Vui lòng nhập số điện thoại")
        LE_address.action.setToolTip("Vui lòng nhập địa chỉ")
        LE_fixing_date.action.setToolTip("Vui lòng nhập ngày sửa chữa")
        
        LE_customer_name.action.setVisible(False)
        LE_VIN_code.action.setVisible(False)
        LE_number_plate.action.setVisible(False)
        LE_phone_number.action.setVisible(False)
        LE_address.action.setVisible(False)
        LE_fixing_date.action.setVisible(False)
        
        LE_customer_name.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_customer_name,
                                                                      event=event)
        LE_VIN_code.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_VIN_code,
                                                                        event=event)
        LE_number_plate.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_number_plate,
                                                                      event=event)
        LE_phone_number.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_phone_number,
                                                                      event=event)
        LE_address.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_address,
                                                                      event=event)
        LE_fixing_date.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_fixing_date,
                                                                        event=event)
    # Hiện xóa    
    def LE_focusOutEvent(UI, self: QLineEdit, event: QFocusEvent):
        if self.text() == "":
            self.action.setVisible(True)
        else:
            self.action.setVisible(False)
        QLineEdit.focusOutEvent(self, event)
        
    # Hiện cảnh báo  
    def setup_foreseen_children(self):
        LT_customer_information: QGridLayout = self.findChild(QGridLayout, "LT_customer_information")
        GB_customer_information: QGroupBox = self.findChild(QGroupBox, "GB_customer_information")
        L_Warning = QLabel(GB_customer_information)
        GB_customer_information.label_warning = L_Warning
        L_Warning.setText("Nhập dữ liệu ")
        LT_customer_information.addWidget(L_Warning,
                            7,
                            0,
                            1,
                            2,
                            Qt.AlignCenter)
        L_Warning.setStyleSheet("QLabel { color : red; }")
        L_Warning.setVisible(False)
        
    def setup_pushButton(self):
        # GB_customer_information QGroupBox
        BT_Ghaph: QPushButton = self.findChild(QPushButton, "BT_Ghaph")
        BT_confirm: QPushButton = self.findChild(QPushButton, "BT_confirm")
        BT_exit: QPushButton = self.findChild(QPushButton, "BT_exit")
        BT_Ghaph.clicked.connect(self.BT_Ghaph_click)
        BT_confirm.clicked.connect(self.BT_confirm_click)
        BT_exit.clicked.connect(self.BT_exit_click)
  
    # Nút chọn ảnh
    def BT_Ghaph_click(self):
        filenames,_ = QtWidgets.QFileDialog.getOpenFileNames()
        self.scene = QtWidgets.QGraphicsScene(self.GV_inciden_images)
        self.GV_inciden_images.setScene(self.scene)
        # Position imge
        pos = [0,0]
        pos_2 = [0,0]
        # Pixel image
        pixel = [690,580]
        # Count number of values in list Filename 
        k = 0
        # Count value in list Filenames
        i = 0
        #Số sảnh đc chọn 
        k = int(len(filenames))
        # Tao list chứa ảnh
        data_list_graph = list(range(0,k))
        # Điều chỉnh ảnh
        for file in filenames:
            img = QtGui.QImage(file)
            data_list_graph[i] = file
            i += 1
            if k <2:
                img = img.scaled(pixel[0], pixel[1])
                Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
                a = self.scene.addItem(Pimax_Item) 
                self.GV_inciden_images.fitInView(Pimax_Item)
            elif k>=2:
                if i <= round(k/2):        
                    img = img.scaled(pixel[0]/round(k/2), pixel[1]/2)
                    Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
                    a = self.scene.addItem(Pimax_Item)
                    Pimax_Item.setOffset(pos[0], pos[1]) 
                    pos[0] += (pixel[0]+5)/round(k/2) 
                elif i > round(k/2):
                    pos_2[1] = (pixel[1]+5)/2
                    img = img.scaled(pixel[0]/(k-round(k/2)),pixel[1]/2)
                    Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
                    a = self.scene.addItem(Pimax_Item)
                    Pimax_Item.setOffset(pos_2[0], pos_2[1])
                    pos_2[0] += (pixel[0]+5)/(k-round(k/2))
        
        data_graph = {'graphic':data_list_graph}
        data_path = os.path.abspath(os.path.join(self.main_path, "data", "data_grap.json"))
        with open(data_path, 'w') as outfile:
            json.dump(data_graph, outfile)
        
                    
    # Nút xác nhận    
    def BT_confirm_click(self):
        LE_customer_name: QLineEdit = self.findChild(QLineEdit, "LE_customer_name")
        LE_VIN_code: QLineEdit = self.findChild(QLineEdit, "LE_VIN_code")
        LE_number_plate: QLineEdit = self.findChild(QLineEdit, "LE_number_plate")
        LE_phone_number: QLineEdit = self.findChild(QLineEdit, "LE_phone_number")
        LE_address: QLineEdit = self.findChild(QLineEdit, "LE_address")
        LE_fixing_date: QLineEdit = self.findChild(QLineEdit, "LE_fixing_date")
        LE_damage: QLineEdit = self.findChild(QLineEdit, "LE_damage")
        
        number_char_vin = int(len(list(LE_VIN_code.text())))
        
        if number_char_vin == 17:
            if LE_customer_name.text() == "" and LE_VIN_code.text() =="" and LE_number_plate.text() =="" and LE_number_plate.text() =="" and LE_phone_number.text() =="" and LE_address.text() =="" and LE_fixing_date.text() =="":
                GB_customer_information: QGroupBox = self.findChild(QGroupBox, "GB_customer_information")
                GB_customer_information.label_warning.setVisible(True)
            else :
                data_cus = {
                    "name": LE_customer_name.text(),
                    "VIN_code": LE_VIN_code.text(),
                    "number_plate": LE_number_plate.text(),
                    "phone_number": LE_phone_number.text(),
                    "address": LE_address.text(),
                    "fixing_date" : LE_fixing_date.text(),
                    "damaged": LE_damage.text()
                }
                data_path = os.path.abspath(os.path.join(self.main_path, "data", "data_cus.json"))
                with open(data_path, 'w') as outfile:
                    json.dump(data_cus, outfile)
                
                file_data = os.path.abspath(os.path.join(self.main_path, "source", "GUImain.py"))
                os.system('python "{}"'.format(file_data))
                
                window.close()
        else:
            GB_customer_information: QGroupBox = self.findChild(QGroupBox, "GB_customer_information")
            GB_customer_information.label_warning.setVisible(True)

    # Đóng chương trình
    def BT_exit_click(self):
        window.close()
        
if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path)
    app.exec_()
