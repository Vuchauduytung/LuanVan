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
        gui_loc = driver.get("path")
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
        
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.childConfig = childConfig_lambda(self)
        self.childConfig(child_prop=driver.get("children"))    
        
            
def childConfig(self, child_prop: dict) -> int:
    if child_prop is None:
        return -1
    else:
        assert isinstance(child_prop, dict), "'child' must be in dict type"
        self.nameless_child = {}
        for name, prop in child_prop.items():
            class_str = prop.get("class")
            CLASS = FormatTranslator.get_class(class_str=class_str)
            assert CLASS is not None, "Unregconize class"
            self.create_object = create_object_lambda(self)
            obj = self.create_object(cls=CLASS, 
                                     name=name)
            icon_prop = prop.get("icon")
            setup_icon(obj=obj, 
                       icon_prop=icon_prop)
                
            geometry_prop = prop.get("geometry")
            setup_geometry(obj=obj, 
                           geometry_prop=geometry_prop)
            font_prop = prop.get("font")
            setup_font(obj=obj, 
                       font_prop=font_prop)
            text = prop.get("text")
            format_str = prop.get("format")
            setup_text(obj=obj, 
                       text=text, 
                       format_str=format_str)
            grid_prop = prop.get("grid")
            self.setup_grid = setup_grid_lambda(self)
            self.setup_grid(obj=obj, 
                            grid_prop=grid_prop)
            visible = prop.get("visible")
            setup_visible(obj=obj, 
                          visible=visible)
            position_prop = prop.get("position")
            size_prop = prop.get("size")
            self.setup_pos_size(obj=obj,
                                position_prop=position_prop,
                                size_prop=size_prop)
            
            if obj.__class__ not in [QGraphicsScene]:
                obj.grid_layout = QGridLayout()
                obj.setLayout(obj.grid_layout)
            obj.childConfig = childConfig_lambda(obj)
            obj.childConfig(child_prop=prop.get("children"))    
        return 0
    
def create_object(self, cls, name):
    obj = self.findChild(cls, name)
    if obj is not None:
        return obj
    else:
        switchers = {
            QLabel: create_named_object_lambda(self),
            QLineEdit: create_named_object_lambda(self),
            QGroupBox: create_named_object_lambda(self),
            QPushButton: create_named_object_lambda(self),
            QCheckBox: create_named_object_lambda(self),
            QGraphicsView: create_named_object_lambda(self),
            QGraphicsScene: create_nameless_object_lambda(self),
            QGraphicsTextItem: create_nameless_object_lambda(self),
            QGraphicsRectItem: create_nameless_object_lambda(self),
            QAction: create_nameless_object_lambda(self)
        }
        self.create_obj = switchers.get(cls)
        return self.create_obj(cls=cls, 
                               name=name)
    
def create_named_object(self, cls, name):
    obj = cls(self)
    obj.setAccessibleName(name)
    return obj

def create_nameless_object(self, cls, name):
    switchers = {
        QGraphicsScene: ("QGraphicsScene", True),
        QGraphicsTextItem: ("QGraphicsTextItem", False),
        QGraphicsRectItem: ("QGraphicsRectItem", False),
        QAction: ("QAction", True)
    }
    choice = switchers.get(cls)
    TYPE = choice[0]
    heritage = choice[1]
    if heritage:
        obj = cls(self)
    else:
        obj = cls()
        self.addItem(obj)
    if TYPE in self.nameless_child.keys():
        self.nameless_child[TYPE].update({
            name: obj
        })
    else:
        self.nameless_child[TYPE] = {
            name: obj
        }
    return obj       
                
def setup_icon(obj, icon_prop) -> int:
    if icon_prop is None:
        return -1
    else:
        icon_name = icon_prop.get("name")
        icon_loc = icon_prop.get("path")
        icon_size = icon_prop.get("size")
        if icon_loc is not None:
            icon_path = os.path.abspath(os.path.join(main_path, icon_name))
            icon = QIcon(icon_path)
            return FormatTranslator.add_icon(obj=obj, 
                                             icon=icon,
                                             size=icon_size)
        else:
            return -1
        
def setup_geometry(obj, geometry_prop) -> int:
    if geometry_prop is None:
        return -1
    else:
        x = geometry_prop.get("x")
        y = geometry_prop.get("y")
        w = geometry_prop.get("w")
        h = geometry_prop.get("h")
        if all(np.array([x, y, w, h]) != None):
            return FormatTranslator.set_geometry(obj=obj,
                                                 x=x, 
                                                 y=y, 
                                                 w=w, 
                                                 h=h)
        else:
            return -1
            
def setup_font(obj, font_prop):
    if font_prop is None:
        return -1
    else:
        fam = font_prop.get("family")
        psz = font_prop.get("pointSize")
        w = font_prop.get("weight")
        itl = font_prop.get("italic")
        if all(np.array([fam , psz, w, itl]) != None):
            return FormatTranslator.set_font(obj=obj, 
                                             fam=fam, 
                                             psz=psz, 
                                             w=w, 
                                             itl=itl)
        else:
            return -1
    
def setup_text(obj, text, format_str):
    if text is None:
        return -1
    else:
        return FormatTranslator.set_text(obj=obj, 
                                         text=text,
                                         format_str=format_str)
            
def setup_grid(self, obj, grid_prop):
    if grid_prop is None:
        return -1
    else:
        row = grid_prop.get("row")
        column = grid_prop.get("column")
        rowSpan = grid_prop.get("rowSpan")
        columnSpan = grid_prop.get("columnSpan")
        alignment = grid_prop.get("alignment")
        if all(np.array([
            row, 
            column,
            rowSpan, 
            columnSpan
        ]) != None):
            if alignment is not None:
                self.grid_layout.addWidget(obj,
                                           row,
                                           column,
                                           rowSpan,
                                           columnSpan,
                                           alignment)
            else:
                self.grid_layout.addWidget(obj,
                                           row,
                                           column,
                                           rowSpan,
                                           columnSpan)
            return 0
        else:
            return -1
            
def setup_visible(obj, visible):
    if visible is None:
        return -1
    else:
        return FormatTranslator.set_visible(obj=obj, 
                                            visible=visible)
        
def setup_pos_size(self, obj, position_prop, size_prop):
    if position_prop is None and size_prop:
        return -1 
    else:
        if size_prop is None:
            size_prop = self.get_size()      
        return FormatTranslator.set_pos_size(obj=obj, 
                                             position=position_prop,
                                             size=size_prop)
        
def childConfig_lambda(self):
    return lambda child_prop: childConfig(self, child_prop)

def setup_grid_lambda(self):
    return lambda obj, grid_prop: setup_grid(self, obj, grid_prop)

def create_object_lambda(self):
    return lambda cls, name: create_object(self, cls, name)    

def create_named_object_lambda(self):
    return lambda cls, name: create_named_object(self, cls, name)    

def create_nameless_object_lambda(self):
    return lambda cls, name: create_nameless_object(self, cls, name)    

                
driver_path = r"E:\AutoProject\source\drivers\GUIinput.json"
path = os.path.abspath(os.path.dirname(__file__))
main_path = os.path.abspath(os.path.join(path, os.pardir))
driver = json2dict(direct_path=driver_path)                
   
        
def main():
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