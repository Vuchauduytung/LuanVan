from PyQt5 import QtWidgets, uic
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from modules.library.IO_support import *
from modules.library.format_translate import *
import numpy as np



class Ui(QtWidgets.QMainWindow):
    
    
    def __init__(self, main_path, driver):
        super(Ui, self).__init__()
        gui_loc = driver.get("directory_path")
        gui_path = os.path.abspath(os.path.join(main_path, gui_loc))
        self.main_path = main_path
        
        ## load GUI
        uic.loadUi(gui_path, self)

        ## GUI config here
        # --------------------------
        self.GUI_init(driver=driver)


        # --------------------------
        
        ## Show GUI and start event loop
        self.show()
        
        
    def GUI_init(self, driver: dict) -> None:
        GUI_name = self.objectName()
        assert GUI_name == driver.get("name"), "GUI name does not match"    
        
        self.desc = driver.get("desc")
        
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        self.childConfig(child_prop=driver.get("children"))    
        
            
    def childConfig(self, child_prop: dict) -> int:
        if child_prop is None:
            return -1
        else:
            assert isinstance(child_prop, dict), "'child' must be in dict type"
            for name, prop in child_prop.items():
                class_str = prop.get("class")
                CLASS = FormatTranslator.get_class(class_str=class_str)
                assert CLASS is not None, "Unregconize class"
                obj = self.findChild(CLASS, name)
                
                icon_prop = prop.get("icon")
                self.setup_icon(obj=obj, 
                                icon_prop=icon_prop)
                
                geometry_prop = prop.get("geometry")
                self.setup_geometry(obj=obj, 
                                    geometry_prop=geometry_prop)
                
            return 0
        
                
    def setup_icon(self, obj, icon_prop) -> int:
        if icon_prop is None:
            return -1
        else:
            icon_name = icon_prop.get("name")
            icon_loc = icon_prop.get("path")
            if icon_loc is not None:
                icon_path = os.path.abspath(os.path.join(self.main_path, icon_name))
                icon = QIcon(icon_path)
                FormatTranslator.add_icon(obj=obj, 
                                          icon=icon)
                return -1
            else:
                return 0
        
    def setup_geometry(self, obj, geometry_prop) -> int:
        if geometry_prop is None:
            return -1
        else:
            x = geometry_prop.get("x")
            y = geometry_prop.get("y")
            w = geometry_prop.get("w")
            h = geometry_prop.get("h")
            if all(np.array([x, y, w, h]) != None):
                FormatTranslator.set_geometry(obj=obj,
                                              x=x, 
                                              y=y, 
                                              w=w, 
                                              h=h)
                return 0
            else:
                return -1
            

        
    

                
                
   
        
def main():
    driver_path = r"E:\AutoProject\source\drivers\GUIinput.json"
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    driver = json2dict(direct_path=driver_path)
    
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path,
                driver=driver)
    app.exec_()
    
    
if __name__ == "__main__":
    main()
    
    # def GUI_init(self):
    #     self.__GB_cus_inf = self.findChild(QGroupBox, "GB_customer_information")
    #     self.__GB_inc_imgs = self.findChild(QGroupBox, "GB_incident_images")
    #     self.__GB_inc_phe = self.findChild(QGroupBox, "GB_incident_phenomena")
        
    #     self.__L_cus_nam = self.findChild(QLabel, "label_customer_name")
    #     self.__L_VIN_cod = self.findChild(QLabel, "label_VIN_code")
    #     self.__L_num_plt = self.findChild(QLabel, "label_number_plate")
    #     self.__L_phn_num = self.findChild(QLabel, "label_phone_number")
    #     self.__L_address = self.findChild(QLabel, "label_address")
    #     self.__L_fix_date = self.findChild(QLabel, "label_fixing_date")
    #     self.__L_warning = self.findChild(QLabel, "label_warning")
        
    #     self.__LE_cus_nam = self.findChild(QLineEdit, "LE_customer_name")
    #     self.__LE_VIN_cod = self.findChild(QLineEdit, "LE_VIN_code")
    #     self.__LE_num_plt = self.findChild(QLineEdit, "LE_number_plate")
    #     self.__LE_phn_num = self.findChild(QLineEdit, "LE_phone_number")
    #     self.__LE_address = self.findChild(QLineEdit, "LE_address")
        
    #     self.__DE_fix_date = self.findChild(QDateEdit, "DE_fixing_date")
                
    #     self.__CB_inc_1 = self.findChild(QCheckBox, "CB_incident_1")
    #     self.__CB_inc_2 = self.findChild(QCheckBox, "CB_incident_2")
    #     self.__CB_inc_3 = self.findChild(QCheckBox, "CB_incident_3")
    #     self.__CB_inc_4 = self.findChild(QCheckBox, "CB_incident_4")
    #     self.__CB_inc_5 = self.findChild(QCheckBox, "CB_incident_5")
    #     self.__CB_inc_6 = self.findChild(QCheckBox, "CB_incident_6")
    #     self.__CB_inc_7 = self.findChild(QCheckBox, "CB_incident_7")
    #     self.__CB_inc_8 = self.findChild(QCheckBox, "CB_incident_8")
    #     self.__CB_inc_9 = self.findChild(QCheckBox, "CB_incident_9")

    #     self.__GV_inc_imgs = self.findChild(QGraphicsView, "GV_inciden_images")
        
    #     self.__BT_confirm = self.findChild(QPushButton, "BT_confirm")
    #     self.__BT_exit = self.findChild(QPushButton, "BT_exit")

    # def GUI_hierarchy(self, driver):
    #     panel_property = driver.get("object")
    #     for ins_name, ins_val in panel_property.items():
    #         if "children" in ins_val.keys():
    #             instance = Items.get_instance(name=ins_name)
    #             child_ins = ins_val.get("children")
    #             self.dequy(ins=instance, 
    #                        child=child_ins)
        
    # def dequy(self, ins, child):
    #     ins_list = []
    #     for key, value in child.items():
    #         instance = Items.get_instance(name=key)
    #         ins_list += [instance]
    #         if "children" in value.keys():
    #             self.dequy(value.get("children"))
    #     ins.child = ins_list       