from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# class FormatTranslator:
#     """
#     Translate json value from string to python class type
#     """
    
#     @staticmethod
#     def get_class(class_str: str):
#         switchers = {
#             "QLabel": QLabel,
#             "QLineEdit": QLineEdit,
#             "QGroupBox": QGroupBox,
#             "QPushButton": QPushButton,
#             "QCheckBox": QCheckBox,
#             "QGraphicsView": QGraphicsView,
#             "QGraphicsScene": QGraphicsScene,
#             "QGraphicsTextItem": QGraphicsTextItem,
#             "QGraphicsRectItem": QGraphicsRectItem,
#             "QAction": QAction,
#         }
#         return switchers.get(class_str)
    
#     @classmethod
#     def add_icon(cls, obj, icon: QIcon):
#         CLASS = obj.__class__
#         switchers = {
#             QLabel: cls.add_icon_use_pixmap(label=obj, 
#                                             icon=icon),
#             QLineEdit: None,
#             QGroupBox: None,
#             QPushButton: obj.setIcon(icon),
#             QCheckBox: obj.setIcon(icon),
#             QGraphicsView: None,
#             QGraphicsScene: None,
#             QGraphicsTextItem: None,
#             QGraphicsRectItem: None
#         }
#         return switchers.get(CLASS)
    
#     @classmethod
#     def set_geometry(cls, obj, x: float, y: float, w: float, h: float):
#         switchers = {
#             QWidget: cls.QWidget_set_geometry,                                
#             QGraphicsItem: cls.QWidget_set_geometry
            
#         }
#         CLASS = obj.__class__
#         set_geometry_function = cls.get_geometry_function_by_class(CLASS=CLASS,
#                                                                    sw=switchers)
#         if set_geometry_function is None:
#             return -1
#         else:
#             return set_geometry_function(obj=obj,
#                                          x=x, 
#                                          y=y, 
#                                          w=w, 
#                                          h=h)
        
#     @classmethod
#     def get_geometry_function_by_class(cls, CLASS, sw: dict):
#         func = None
#         if CLASS in sw.keys():
#             func = sw.get(CLASS)
#         elif CLASS is None:
#             pass
#         else:
#             for CLASS_ in CLASS.__bases__:
#                 if func is None:
#                     func = sw.get(CLASS_)
#         return func
                

class QGraphicsTextItem_callback:
    
    def __init__(self, curs_min: float, curs_max: float):
        self.curs_min = curs_min
        self.curs_max = curs_max
        

        
        
                                          
            
        
        
        