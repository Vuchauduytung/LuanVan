from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import numpy as np
# Import json module
from modules.library.IO_support import *
from modules.library.Open_pdf import *
from modules.library.compare import *
import webbrowser

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
        self.setup_lineEdit_diagnose()
        self.show()
    
    def open_json(self):
        #Open json
        data_path = os.path.abspath(os.path.join(self.main_path, "data", "data_cus.json"))
        customer = json2dict(data_path)
        
    def setup_lineEdit_information_custom(self):
        #Open json
        data_path = os.path.abspath(os.path.join(self.main_path, "data", "data_cus.json"))
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
        LE_name.setText(customer["name"])
        LE_num_vin.setText(customer["VIN_code"])
        LE_lices_num.setText(customer["number_plate"])
        LE_num_phone.setText(customer["phone_number"])
        LE_address.setText(customer["address"])
        LE_date_fix.setText(customer["fixing_date"])
        LE_fix_car.setText(customer["damaged"])
        
    def setup_lineEdit_car_number_VIN(self):
        #Open json
        data_path = os.path.abspath(os.path.join(self.main_path, "data", "data_cus.json"))
        customer = json2dict(data_path)
        vin_num = list(customer["VIN_code"])
        vin_num_product = "".join(vin_num[:3])
        vin_num_product_2 = "".join(vin_num[:2])
        num_product = "".join(vin_num[11:])
        
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
        vin_product = num_vin_data["name_product_car"]["value"].get(vin_num_product)
        vin_product_2 = num_vin_data["name_product_car"]["value"].get(vin_num_product_2)
        if isinstance(vin_product, dict) and vin_product != None:
            if vin_num_product == vin_product.get("key"):
                LE_car_model.setText(vin_product.get("text"))
                LE_car_name.setText(vin_product.get("text"))
            elif vin_num_product_2 == vin_product_2.get("key"):
                LE_car_model.setText(vin_product_2.get("text"))
                LE_car_name.setText(vin_product_2.get("text"))
            else:   
                LE_car_model.setText("Not assigned")
                LE_car_name.setText("Not assigned")
        else:   
            LE_car_model.setText("Not assigned")
            LE_car_name.setText("Not assigned")    
        LE_sec_num.setText(vin_num[8])
        LE_product_date.setText(num_vin_data["product_date"]["value"][vin_num[6]]["text"])
        LE_factory.setText(vin_num[10])
        LE_num_product.setText(num_product)
    
    def setup_lineEdit_diagnose(self):
        data_path = os.path.abspath(os.path.join(self.main_path, "data" ,"data_cus_pdf.json"))
        error = json2dict(data_path)
        
        num_xilanh = 0
        for num_xilanh in range(0,4):
            num_xilanh +=1
            
            xilanh_str = "Xylanh_{}".format(num_xilanh)
            
            Pmax = error[xilanh_str]["Pmax"]
            compression_pressure = error[xilanh_str]["compression_pressure"]
            Minimum_pressure_intake = error[xilanh_str]["Minimum_pressure_intake"]
            Pmin = error[xilanh_str]["Pmin"]
            
            value_str, damage_c_str = compare_c(compression_pressure = compression_pressure ,
                        Pmax = Pmax ,
                        Pmin = Pmin ,
                        Minimum_pressure_intake = Minimum_pressure_intake)
            
            value_in_str, damage_in_str = compare_in(compression_pressure = compression_pressure ,
                        Pmax = Pmax ,
                        Pmin = Pmin ,
                        Minimum_pressure_intake = Minimum_pressure_intake)
            
            if value_str == "Bình thường" and value_in_str == "Bình thường":
                assess_str = """
                <h3>Trạng thái:</h3>
                <p>&ensp;{xilanh}</p>
                <p>&ensp;{value}</p>
                """\
                    .format(xilanh=xilanh_str,
                            value=value_str)
                TE_diagnoses: QTextEdit = self.findChild(QTextEdit, "TE_diagnose_{num}"\
                    .format(num=num_xilanh))
                TE_diagnoses.setHtml(assess_str)
            elif value_str == 'Hư hỏng':
                assess_str = """
                <h3>Trạng thái:</h3>
                <p>&ensp;{xilanh}</p>
                <p>&ensp;{value}</p>
                <p>&ensp;{damage}</p>
                """\
                    .format(xilanh=xilanh_str,
                            value=value_str,
                            damage=damage_c_str)
                TE_diagnoses: QTextEdit = self.findChild(QTextEdit, "TE_diagnose_{num}"\
                    .format(num=num_xilanh))
                TE_diagnoses.setHtml(assess_str)
            elif value_in_str == 'Hư hỏng':
                assess_str = """
                <h3>Trạng thái:</h3>
                <p>&ensp;{xilanh}</p>
                <p>&ensp;{value}</p>
                <p>&ensp;{damage_in}</p>
                """\
                    .format(xilanh=xilanh_str,
                            value=value_in_str,
                            damage_in=damage_in_str)
                TE_diagnoses: QTextEdit = self.findChild(QTextEdit, "TE_diagnose_{num}"\
                    .format(num=num_xilanh))
                TE_diagnoses.setHtml(assess_str)
            elif value_str =='Hư hỏng' and value_in_str == 'Hư hỏng':
                assess_str = """
                <h3>Trạng thái:</h3>
                <p>&ensp;{xilanh}</p>
                <p>&ensp;{value}</p>
                <p>&ensp;{damage}</p>
                <p>&ensp;{damage_in}</p>
                """\
                    .format(xilanh=xilanh_str,
                            value=value_in_str,
                            damage=damage_c_str,
                            damage_in=damage_in_str)
                TE_diagnoses: QTextEdit = self.findChild(QTextEdit, "TE_diagnose_{num}"\
                    .format(num=num_xilanh))
                TE_diagnoses.setHtml(assess_str)
        
        
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
        
        file_data = os.path.abspath(os.path.join(self.main_path, "source", "GUIgraph_xylanh_1.py"))
        os.system('python "{}"'.format(file_data))
        file_data = os.path.abspath(os.path.join(self.main_path, "source", "GUIgraph_xylanh_2.py"))
        os.system('python "{}"'.format(file_data))
        file_data = os.path.abspath(os.path.join(self.main_path, "source", "GUIgraph_xylanh_3.py"))
        os.system('python "{}"'.format(file_data))
        file_data = os.path.abspath(os.path.join(self.main_path, "source", "GUIgraph_xylanh_4.py"))
        os.system('python "{}"'.format(file_data))
        
    def BT_fix_click(self):
        
        data_path = os.path.abspath(os.path.join(self.main_path, "data" ,"data_cus_pdf.json"))
        pdf = json2dict(data_path)

        num_xilanh = 0
        for num_xilanh in range(0,4):
            num_xilanh +=1
            
            xilanh_str = "Xylanh_{}".format(num_xilanh)
            
            Pmax = pdf[xilanh_str]["Pmax"]
            compression_pressure = pdf[xilanh_str]["compression_pressure"]
            Minimum_pressure_intake = pdf[xilanh_str]["Minimum_pressure_intake"]
            Pmin = pdf[xilanh_str]["Pmin"]
        
            value, path_open, path= open_c(compression_pressure = compression_pressure ,
                            Pmax = Pmax ,
                            Pmin = Pmin ,
                            Minimum_pressure_intake = Minimum_pressure_intake)
            
            value_in, path_open_in, path_in = open_in(compression_pressure = compression_pressure ,
                            Pmax = Pmax ,
                            Pmin = Pmin ,
                            Minimum_pressure_intake = Minimum_pressure_intake)
            
            if value == "Bình thường" and value_in == "Bình thường":
                webbrowser.open_new(path_open)
            elif value == 'Hư hỏng':
                webbrowser.open_new(path_open)
                webbrowser.open_new(path)
            elif value_in == 'Hư hỏng':
                webbrowser.open_new(path_open)
                webbrowser.open_new(path_in)
            elif value =='Hư hỏng' and value_in == 'Hư hỏng':
                webbrowser.open_new(path_open)
                webbrowser.open_new(path)
                webbrowser.open_new(path_in)
        
    def BT_cancel_click(self):
        window.close()
        
    

if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path)
    app.exec_()
