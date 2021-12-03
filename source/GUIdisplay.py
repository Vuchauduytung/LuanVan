from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import numpy as np
# Import json module
from modules.library.IO_support import *

class Ui(QtWidgets.QMainWindow):
    """
    Application
    """

    def __init__(self, main_path):
        super(Ui, self).__init__()
        self.main_path = main_path
        # load GUI
        gui_path = os.path.abspath(
            os.path.join(main_path, "GUI", "GUIdisplay.ui"))
        uic.loadUi(gui_path, self)
        self.setup_pushButton()
        self.setup_lineEdit_information_custom()
        self.setup_lineEdit_car_number_VIN()
        self.show()
    
    def open_json(self):
        #Open json
        data_path = os.path.abspath(os.path.join(self.main_path, "source", "data.json"))
        customer = json2dict(data_path)
        
    def setup_lineEdit_information_custom(self):
        #Open json
        data_path = os.path.abspath(os.path.join(self.main_path, "source", "data.json"))
        customer = json2dict(data_path)
        
        GB_information_custom: QGroupBox = self.findChild(QGroupBox, "GB_information_custom")
        LE_name: QLineEdit = self.findChild(QLineEdit, "LE_name")
        LE_num_vin: QLineEdit = self.findChild(QLineEdit, "LE_num_vin")
        LE_lices_num: QLineEdit = self.findChild(QLineEdit, "LE_lices_num")
        LE_num_phone: QLineEdit = self.findChild(QLineEdit, "LE_num_phone")
        LE_address: QLineEdit = self.findChild(QLineEdit, "LE_address")
        LE_date_fix: QLineEdit = self.findChild(QLineEdit, "LE_date_fix")
        LE_fix_car: QLineEdit = self.findChild(QLineEdit, "LE_fix_car")
        
        #Hien gia tri
        LE_name.setText(customer["durian"])
        LE_num_vin.setText(customer["durian"])
        LE_lices_num.setText(customer["durian"])
        LE_num_phone.setText(customer["durian"])
        LE_address.setText(customer["durian"])
        LE_date_fix.setText(customer["durian"])
        LE_fix_car.setText(customer["durian"])
        
    def setup_lineEdit_car_number_VIN(self):
        #Open json
        data_path = os.path.abspath(os.path.join(self.main_path, "source", "data.json"))
        customer = json2dict(data_path)
        vin_num = list(customer["num_vin"])
        vin_num_product = "".join(vin_num[:3])
        print(vin_num)
        
        data_vin = os.path.abspath(os.path.join(self.main_path, "source","library", "libary_VIN.json"))
        num_vin_data = json2dict(data_vin)
        # Doc ma vin
        GB_car_number_VIN: QGroupBox = self.findChild(QGroupBox, "GB_car_number_VIN")
        LE_area: QLineEdit = self.findChild(QLineEdit, "LE_area")    
        LE_country: QLineEdit = self.findChild(QLineEdit, "LE_country")
        LE_car_model: QLineEdit = self.findChild(QLineEdit, "LE_car_model")
        LE_car_name: QLineEdit = self.findChild(QLineEdit, "LE_car_name")
        LE_sec_num: QLineEdit = self.findChild(QLineEdit, "LE_sec_num")
        LE_product_date: QLineEdit = self.findChild(QLineEdit, "LE_product_date")
        LE_factory: QLineEdit = self.findChild(QLineEdit, "LE_factory")
        LE_num_product: QLineEdit = self.findChild(QLineEdit, "LE_num_product")
        
        #Hien gia tri
        LE_area.setText(num_vin_data["contry"]["value"][vin_num[0]]["text"])
        LE_country.setText(num_vin_data["contry"]["value"][vin_num[0]]["children"][vin_num[1]]["text"])
        LE_car_model.setText(num_vin_data["name_product_car"]["value"][vin_num_product]["text"])
        LE_car_name.setText(num_vin_data["name_product_car"]["value"][vin_num_product]["text"])
        LE_sec_num.setText(customer["phone"])
        LE_product_date.setText(num_vin_data["product_date"]["value"][vin_num[6]]["text"])
        LE_factory.setText(customer["phone"])
        LE_num_product.setText(customer["phone"])
        
        
    def LE_focusOutEvent(UI, self: QLineEdit, event: QFocusEvent):
        if self.text() == "":
            self.action.setVisible(True)
        else:
            self.action.setVisible(False)
        QLineEdit.focusOutEvent(self, event)
        
    def setup_pushButton(self):
        # GB_informatin_custom QGroupBox
        BT_graph_fix: QPushButton = self.findChild(QPushButton, "BT_graph_fix")
        BT_graph_fix.clicked.connect(self.BT_graph_fix_click)
        
        BT_graph: QPushButton = self.findChild(QPushButton, "BT_graph")
        BT_graph.clicked.connect(self.BT_graph_click)
        
        BT_fix: QPushButton = self.findChild(QPushButton, "BT_fix")
        BT_fix.clicked.connect(self.BT_fix_click)
        
        BT_cancel: QPushButton = self.findChild(QPushButton, "BT_cancel")
        BT_cancel.clicked.connect(self.BT_cancel_click)
        
    def BT_graph_fix_click(self):
        file_data = os.path.abspath(os.path.join(self.main_path, "source", "GUIgraph_fix.py"))
        os.system('python "{}"'.format(file_data))
        
    def BT_graph_click(self):
        file_data = os.path.abspath(os.path.join(self.main_path, "source", "GUIgraph_xylanh.py"))
        os.system('python "{}"'.format(file_data))
        
    def BT_fix_click(self):
        file_data = os.path.abspath(os.path.join(self.main_path, "source","modules","library","Open_pdf.py"))
        os.system('python "{}"'.format(file_data))
        
    def BT_cancel_click(self):
        window.close()
        
    

if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path)
    app.exec_()
