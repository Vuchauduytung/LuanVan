from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class FormatTranslator:
    """
    Translate json value from string to python class type
    """
    
    @staticmethod
    def get_class(class_str: str):
        switchers = {
            "QLabel": QLabel,
            "QLineEdit": QLineEdit,
            "QGroupBox": QGroupBox,
            "QPushButton": QPushButton,
            "QCheckBox": QCheckBox,
            "QGraphicsView": QGraphicsView,
            "QGraphicsScene": QGraphicsScene,
            "QGraphicsTextItem": QGraphicsTextItem,
            "QGraphicsRectItem": QGraphicsRectItem,
            "QAction": QAction,
        }
        return switchers.get(class_str)
    
    @classmethod
    def add_icon(cls, obj, icon: QIcon, size: list):
        CLASS = obj.__class__
        switchers = {
            QLabel: cls.add_icon_use_pixmap,
            QLineEdit: None,
            QGroupBox: None,
            QPushButton: lambda _, __, icon: obj.setIcon(icon),
            QCheckBox: lambda _, __, icon: obj.setIcon(icon),
            QGraphicsView: None,
            QGraphicsScene: None,
            QGraphicsTextItem: None,
            QGraphicsRectItem: None,
            QAction: lambda _, __, icon: obj.setIcon(icon),
        }
        FUNCTION = switchers.get(CLASS)
        if FUNCTION is None:
            return -1
        else:
            return FUNCTION(label=obj,
                            size=size,
                            icon=icon)
    
    @classmethod
    def set_geometry(cls, obj, x: float, y: float, w: float, h: float):
        switchers = {
            QWidget: cls.QWidget_set_geometry,                                
            QGraphicsItem: cls.QGraphicsItem_set_geometry    
        }
        CLASS = obj.__class__
        set_geometry_function = cls.get_geometry_function_by_class(CLASS=CLASS,
                                                                   sw=switchers)
        if set_geometry_function is None:
            return -1
        else:
            set_geometry_function(obj=obj,
                                  x=x, 
                                  y=y, 
                                  w=w, 
                                  h=h)
            return 0
        
    @classmethod
    def get_geometry_function_by_class(cls, CLASS, sw: dict):
        func = None
        if CLASS in sw.keys():
            func = sw.get(CLASS)
        elif CLASS is None:
            pass
        else:
            for CLASS_ in CLASS.__bases__:
                if func is None:
                    func = sw.get(CLASS_)
        return func
    
    @classmethod
    def set_font(cls, obj, fam: str, psz: int, w: int, itl: bool):
        font = QFont(family=fam,
                     pointSize=psz,
                     weight=w,
                     italic=itl)
        CLASS = obj.__class__
        switchers = {
            QLabel: lambda font: obj.setFont(font),
            QLineEdit: lambda font: obj.setFont(font),
            QGroupBox:lambda font: obj.setFont(font),
            QPushButton: lambda font: obj.setFont(font),
            QCheckBox: lambda font: obj.setFont(font),
            QGraphicsView: None,
            QGraphicsScene: None,
            QGraphicsTextItem: None,
            QGraphicsRectItem: None,
            QAction: lambda font: obj.setFont(font),
        }
        FUNCTION = switchers.get(CLASS)
        if FUNCTION is None:
            return -1
        else:
            FUNCTION(font)
            return 0
    
    @classmethod
    def set_text(cls, obj, text, format_str):
        CLASS = obj.__class__
        switchers = {
            QLabel: cls.QLabel_set_text,
            QLineEdit: lambda _, text, __: obj.setText(text),
            QGroupBox: lambda _, text, __: obj.setTitle(text),
            QPushButton: lambda _, text, __: obj.setText(text),
            QCheckBox: lambda _, text, __: obj.setText(text),
            QGraphicsView: None,
            QGraphicsScene: None,
            QGraphicsTextItem: cls.QGraphicsText_set_text,
            QGraphicsRectItem: None,
            QAction: lambda _, text, __: obj.setTitle(text),
        }
        FUNCTION = switchers.get(CLASS)
        if FUNCTION is None:
            return -1
        else:
            return FUNCTION(obj, 
                            text,
                            format_str)
    
    @classmethod
    def set_visible(cls, obj, visible):
        CLASS = obj.__class__
        switchers = {
            QLabel: cls.show_hide,
            QLineEdit: cls.show_hide,
            QGroupBox: cls.show_hide,
            QPushButton: cls.show_hide,
            QCheckBox: cls.show_hide,
            QGraphicsView: None,
            QGraphicsScene: None,
            QGraphicsTextItem: lambda visible: obj.setVisible(visible),
            QGraphicsRectItem: lambda visible: obj.setVisible(visible),
            QAction: lambda visible: obj.setVisible(visible),
        }
        FUNCTION = switchers.get(CLASS)
        if FUNCTION is None:
            return -1
        else:
            return FUNCTION(obj, 
                            visible)

    @classmethod
    def add_icon_use_pixmap(cls, label, size, icon):
        pixmap = icon.pixmap(QSize(size[0], size[1]))
        label.setPixmap(pixmap)
        return 0
        
    @classmethod
    def QWidget_set_geometry(cls, obj, x, y, w, h):
        obj.setGeometry(x, 
                        y, 
                        w, 
                        h)                              
        return 0       
                              
    @classmethod
    def QGraphicsItem_set_geometry(cls, obj, x, y, w, h):
        obj.update(x=x, 
                   y=y, 
                   width=w, 
                   height=h)                              
        return 0  
    
    @classmethod
    def QLabel_set_text(cls, obj, text, format_str):
        obj.setText(text)
        switchers = {
            "PlainText": Qt.PlainText,
            "RichText": Qt.RichText,
            "AutoText": Qt.AutoText,
            "MarkdownText": Qt.MarkdownText
        }
        FORMAT = switchers.get(format_str)
        if FORMAT is None:
            return -1
        else:
            obj.setTextFormat(FORMAT)
            return 0
           
    @classmethod                 
    def QGraphicsText_set_text(cls, obj, text, format_str):
        switchers = {
            "PlainText": obj.insertText(text),
            "RichText": obj.insertHtml(text),
            "AutoText": None,
            "MarkdownText": None,
        }
        switchers.get(format_str)
        return 0     
    
    @classmethod
    def show_hide(cls, obj, visible):
        if visible:
            obj.show()
        else:
            obj.hide()
        return 0
    
    @classmethod
    def set_pos_size(cls, obj, position, size):
        switchers = {
            
        }
    

class QGraphicsTextItem_callback:
    
    def __init__(self, curs_min: float, curs_max: float):
        self.curs_min = curs_min
        self.curs_max = curs_max
        

        
        
                                          
            
        
        
        