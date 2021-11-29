from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from task import *
from method_support import *


class PyQtSupport:
    """
    Class này hỗ trợ biên dịch các yêu cầu liên quan đến Object
    Widget trong PyQt Application.
    """

    @staticmethod
    def get_class(cls_name: str):
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
            "QDateEdit": QDateEdit,
        }
        return switchers.get(cls_name)

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
            QDateEdit: None,
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
        set_geometry_function = cls.get_value_from_base_class(CLASS=CLASS,
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
    def get_size(cls, obj):
        return cls.get_rect(obj)

    @classmethod
    def get_value_from_base_class(cls, CLASS, sw: dict):
        func = None
        if CLASS in sw.keys():
            func = sw.get(CLASS)
        elif CLASS is None:
            return
        else:
            for CLASS_ in CLASS.__bases__:
                if func is None:
                    func = sw.get(CLASS_)
                    if func is None:
                        func = cls.get_value_from_base_class(CLASS=CLASS_,
                                                             sw=sw)
        return func

    @staticmethod
    def set_font(obj, fam: str, psz: int, w: int, itl: bool):
        font = QFont(fam,
                     psz,
                     w,
                     itl)
        CLASS = obj.__class__
        switchers = {
            QLabel: lambda font: obj.setFont(font),
            QLineEdit: lambda font: obj.setFont(font),
            QGroupBox: lambda font: obj.setFont(font),
            QPushButton: lambda font: obj.setFont(font),
            QCheckBox: lambda font: obj.setFont(font),
            QGraphicsView: None,
            QGraphicsScene: None,
            QGraphicsTextItem: None,
            QGraphicsRectItem: None,
            QAction: lambda font: obj.setFont(font),
            QDateEdit: lambda font: obj.setFont(font),
        }
        FUNCTION = switchers.get(CLASS)
        if FUNCTION is None:
            return -1
        else:
            FUNCTION(font)
            return 0

    @classmethod
    def set_text(cls, obj, text: str, format_str: str):
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
            QDateEdit: lambda _, text, __: obj.setText(text),
        }
        FUNCTION = switchers.get(CLASS)
        if FUNCTION is None:
            return -1
        else:
            return FUNCTION(obj,
                            text,
                            format_str)

    @classmethod
    def set_visible(cls, obj, visible: bool):
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
            QDateEdit: cls.show_hide,
        }
        FUNCTION = switchers.get(CLASS)
        if FUNCTION is None:
            return -1
        else:
            return FUNCTION(obj,
                            visible)

    @staticmethod
    def add_icon_use_pixmap(label, size: list, icon: QIcon):
        pixmap = icon.pixmap(QSize(size[0], size[1]))
        label.setPixmap(pixmap)
        return 0

    @staticmethod
    def QWidget_set_geometry(obj, x: float, y: float, w: float, h: float):
        obj.setGeometry(x,
                        y,
                        w,
                        h)
        return 0

    @staticmethod
    def QGraphicsItem_set_geometry(obj, x: float, y: float, w: float, h: float):
        obj.update(x=x,
                   y=y,
                   width=w,
                   height=h)
        return 0

    @staticmethod
    def QLabel_set_text(obj, text: str, format_str: str):
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

    @staticmethod
    def QGraphicsText_set_text(obj, text: str, format_str: str):
        switchers = {
            "PlainText": obj.setPlainText,
            "RichText": obj.setHtml,
            "AutoText": None,
            "MarkdownText": None,
        }
        FUNCTION = switchers.get(format_str)
        if FUNCTION is not None:
            FUNCTION(text)
        return 0

    @staticmethod
    def show_hide(obj, visible: bool):
        if visible:
            obj.show()
        else:
            obj.hide()
        return 0

    @staticmethod
    def set_pos_size(obj, position: list, size: list):
        obj.setTransformOriginPoint(size[0], size[1])
        obj.update(position[0],
                   position[1],
                   size[0],
                   size[1])
        return 0
    
    @classmethod
    def get_rect(cls, obj):
        switchers = {
            QLabel: lambda obj: obj.geometry(),
            QLineEdit: lambda obj: obj.geometry(),
            QGroupBox: lambda obj: obj.geometry(),
            QPushButton: lambda obj: obj.geometry(),
            QCheckBox: lambda obj: obj.geometry(),
            QGraphicsView: lambda obj: obj.geometry(),
            QGraphicsScene: lambda scene: scene.sceneRect(),
            QGraphicsTextItem: lambda text_item: cls.QGraphicsTextItem_get_rect(text_item),
            QGraphicsRectItem: lambda rect_item: rect_item.rect(),
            QAction: None,
            QDateEdit: lambda obj: obj.geometry(),
        }
        FUNCTION = switchers.get(obj.__class__)
        if FUNCTION is None:
            return None
        else:
            rect = FUNCTION(obj)
            return rect
        
    @staticmethod
    def QGraphicsTextItem_get_rect(text_item: QGraphicsTextItem):
        size = text_item.document().size()
        x = text_item.x()
        y = text_item.y()
        return QRect(x, 
                     y, 
                     size.width(), 
                     size.height)
        
    @classmethod
    def set_scale(cls, obj, parent_rect: QRect, scale: float):
        switchers = {
            QGraphicsItem: cls.QGraphicsItem_set_scale
        }
        FUNCTION = PyQtSupport.get_value_from_base_class(CLASS=obj.__class__,
                                                         sw=switchers)
        assert FUNCTION is not None, "class {cls} doesn't have scale property"\
            .format(cls=obj.__class__)
        return FUNCTION(obj,
                        parent_rect,
                        scale)

    @classmethod
    def QGraphicsItem_set_scale(cls, obj, parent_rect: QRect, scale: float):
        switchers = {
            QGraphicsTextItem: cls.QGraphicsTextItem_set_rect,
            QGraphicsRectItem: lambda obj, parent_rect: obj.setRect(parent_rect),
        }
        origin = MethodSupport.get_origin(parent_rect)
        obj.setTransformOriginPoint(origin)
        CLASS = obj.__class__
        FUNCTION = switchers.get(CLASS)
        FUNCTION(obj, parent_rect)
        obj.setScale(scale)
        return 0
        
    @staticmethod
    def QGraphicsTextItem_set_rect(obj, rect: QRect):
        obj.setPos(rect.x(),
                   rect.y())
        obj.document().setPageSize(QSizeF(rect.width(),
                                   rect.height()))
        return 0
    
    @classmethod
    def create_object(cls, UI, CLASS, name: str, parent):
        switchers = {
            QLabel: (lambda CLASS, name, parent: cls.create_named_object(UI, 
                                                                         CLASS, 
                                                                         name, 
                                                                         parent)),
            QLineEdit: (lambda CLASS, name, parent: cls.create_named_object(UI, 
                                                                            CLASS, 
                                                                            name, 
                                                                            parent)),
            QGroupBox: (lambda CLASS, name, parent: cls.create_named_object(UI, 
                                                                            CLASS, 
                                                                            name, 
                                                                            parent)),
            QPushButton: (lambda CLASS, name, parent: cls.create_named_object(UI, 
                                                                            CLASS, 
                                                                            name, 
                                                                            parent)),
            QCheckBox: (lambda CLASS, name, parent: cls.create_named_object(UI, 
                                                                            CLASS, 
                                                                            name, 
                                                                            parent)),
            QGraphicsView: (lambda CLASS, name, parent: cls.create_named_object(UI, 
                                                                                CLASS, 
                                                                                name, 
                                                                                parent)),
            QGraphicsScene: (lambda CLASS, name, parent: cls.create_nameless_object(UI, 
                                                                                    CLASS, 
                                                                                    name, 
                                                                                    parent)),
            QGraphicsTextItem: (lambda CLASS, name, parent: cls.create_nameless_object(UI, 
                                                                                       CLASS, 
                                                                                       name, 
                                                                                       parent)),
            QGraphicsRectItem: (lambda CLASS, name, parent: cls.create_nameless_object(UI, 
                                                                                       CLASS, 
                                                                                       name, 
                                                                                       parent)),
            QAction: (lambda CLASS, name, parent: cls.create_nameless_object(UI, 
                                                                             CLASS, 
                                                                             name, 
                                                                             parent)),
            QDateEdit: (lambda CLASS, name, parent: cls.create_named_object(UI, 
                                                                            CLASS, 
                                                                            name, 
                                                                            parent))
        }
        UI.create_obj = switchers.get(CLASS)
        return UI.create_obj(CLASS,
                             name,
                             parent)
        
    @staticmethod
    def create_named_object(_, cls, name: str, parent):
        obj = cls(parent)
        obj.setAccessibleName(name)
        return obj

    @staticmethod
    def create_nameless_object(UI, cls, name: str, parent):
        switchers = {
            QGraphicsScene: True,
            QGraphicsTextItem: False,
            QGraphicsRectItem: False,
            QAction: True
        }
        heritage = switchers.get(cls)
        if heritage:
            obj = cls(parent)
            if obj.__class__ in [QGraphicsScene]:
                parent: QGraphicsView
                parent.setScene(obj)
        else:
            parent: QGraphicsScene
            obj = cls()
            parent.addItem(obj)
        if parent.__class__ in [QGraphicsView]:
            size = parent.size()
            obj.setSceneRect(size.width()*0.01,
                            size.height()*0.01,
                            size.width()*0.98,
                            size.height()*0.98)
        else:
            pass
        if cls in UI.nameless_child.keys():
            UI.nameless_child[cls].update({
                name: obj
            })
        else:
            UI.nameless_child[cls] = {
                name: obj
            }
        return obj

    @staticmethod
    def get_object(UI, CLASS, name):
        switchers = {
            QLabel: lambda CLASS, name: UI.findChild(CLASS, name),
            QLineEdit: lambda CLASS, name: UI.findChild(CLASS, name),
            QGroupBox: lambda CLASS, name: UI.findChild(CLASS, name),
            QPushButton: lambda CLASS, name: UI.findChild(CLASS, name),
            QCheckBox: lambda CLASS, name: UI.findChild(CLASS, name),
            QGraphicsView: lambda CLASS, name: UI.findChild(CLASS, name),
            QGraphicsScene: lambda CLASS, name: UI.nameless_child.get(CLASS).get(name),
            QGraphicsTextItem: lambda CLASS, name: UI.nameless_child.get(CLASS).get(name),
            QGraphicsRectItem: lambda CLASS, name: UI.nameless_child.get(CLASS).get(name),
            QAction: lambda CLASS, name: UI.nameless_child.get(CLASS).get(name),
            QDateEdit: lambda CLASS, name: UI.findChild(CLASS, name)
        }
        FUNCTION = switchers.get(CLASS)
        if FUNCTION is None:
            return None
        else:
            return FUNCTION(CLASS=CLASS,
                            name=name)