from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import numpy as np
from modules.library.IO_support import *
from modules.library.pyqt_support import *
from modules.library.pyqt_event import *
from task import *

def childConfig(self, child_prop: dict, GUI, main_path: str):
    if child_prop is None:
        return -1
    else:
        assert isinstance(child_prop, dict), "'child' must be in dict type"
        self.nameless_child = {}
        self.create_object = create_object_lambda(self)
        self.setup_grid = setup_grid_lambda(self)
        for name, prop in child_prop.items():
            class_str = prop.get("class")
            CLASS = PyQtSupport.get_class(class_str=class_str)
            assert CLASS is not None, "Unregconize class"

            obj = self.create_object(cls=CLASS,
                                     name=name)

            icon_prop = prop.get("icon")
            setup_icon(obj=obj,
                       icon_prop=icon_prop,
                       main_path=main_path)

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

            self.setup_grid(obj=obj,
                            grid_prop=grid_prop)
            visible = prop.get("visible")
            setup_visible(obj=obj,
                          visible=visible)
            position_prop = prop.get("position")
            size_prop = prop.get("size")
            obj.setup_pos_size = setup_pos_size_lambda(obj)
            obj.setup_pos_size(obj=obj,
                               position_prop=position_prop,
                               size_prop=size_prop)
            action_prop = prop.get("action")
            obj.setup_action = setup_action_lambda(obj)
            obj.setup_action(action_prop=action_prop,
                             main_path=main_path)
            date = prop.get("date")
            minimum_date = prop.get("minimum_date")
            maximum_date = prop.get("maximum_date")
            callback_prop = prop.get("callback")
            document = prop.get("document")
            obj.setup_document = setup_document_lambda(obj)
            obj.setup_document(document=document)
            obj.setup_callback = setup_callback_lambda(obj)
            obj.setup_callback(callback_prop=callback_prop,
                               GUI=GUI)
            obj.setup_date = setup_date_lambda(obj)
            obj.setup_date(date_str=date,
                           minimum_date_str=minimum_date,
                           maximum_date_str=maximum_date)

            if obj.__class__ not in [QGraphicsScene, QGraphicsTextItem, QGraphicsRectItem]:
                obj.grid_layout = QGridLayout()
                obj.setLayout(obj.grid_layout)
            obj.childConfig = childConfig_lambda(obj)
            obj.childConfig(child_prop=prop.get("children"),
                            GUI=GUI,
                            main_path=main_path)
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
            QAction: create_nameless_object_lambda(self),
            QDateEdit: create_named_object_lambda(self)
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
    if obj.__class__ in [QGraphicsScene]:
        self.setScene(obj)
    if TYPE in self.nameless_child.keys():
        self.nameless_child[TYPE].update({
            name: obj
        })
    else:
        self.nameless_child[TYPE] = {
            name: obj
        }
    return obj


def setup_icon(obj, icon_prop, main_path):
    if icon_prop is None:
        return -1
    else:
        icon_name = icon_prop.get("name")
        icon_loc = icon_prop.get("path")
        icon_size = icon_prop.get("size")
        if icon_loc is not None:
            icon_path = os.path.abspath(os.path.join(main_path, icon_name))
            icon = QIcon(icon_path)
            return PyQtSupport.add_icon(obj=obj,
                                        icon=icon,
                                        size=icon_size)
        else:
            return -1


def setup_geometry(obj, geometry_prop):
    if geometry_prop is None:
        return -1
    else:
        x = geometry_prop.get("x")
        y = geometry_prop.get("y")
        w = geometry_prop.get("w")
        h = geometry_prop.get("h")
        if all(np.array([x, y, w, h]) != None):
            return PyQtSupport.set_geometry(obj=obj,
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
        if any(np.array([fam, psz, w, itl]) != None):
            if fam is None:
                fam = obj.font().defaultFamily()
            if psz is None:
                psz = -1
            if w is None:
                w = -1
            if itl is None:
                itl = False
            return PyQtSupport.set_font(obj=obj,
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
        return PyQtSupport.set_text(obj=obj,
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
            # obj.setParent(None)
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
        return PyQtSupport.set_visible(obj=obj,
                                       visible=visible)


def setup_pos_size(self, obj, position_prop, size_prop):
    if position_prop is None and size_prop is None:
        return -1
    else:
        parent_size = PyQtSupport.get_size(self)
        switchers = {
            "Up-Left": (0, 0),
            "Up-Center": (parent_size[0]/2, 0),
            "Up-Right": (parent_size[0], 0),
            "Center-Right": (parent_size[0], parent_size[1]/2),
            "Down-Right": (parent_size[0], parent_size[1]),
            "Down-Center": (parent_size[0]/2, parent_size[1]),
            "Down-Left": (0, parent_size[1]),
            "Center-Left": (0, parent_size[1]/2),
            "Center-Center": (parent_size[0]/2, parent_size[1]/2)
        }
        position = switchers.get(position_prop)
        if size_prop is None:
            size = parent_size
        else:
            size = size_prop
        return PyQtSupport.set_pos_size(obj=obj,
                                        position=position,
                                        size=size)


def setup_action(self, action_prop, main_path: str):
    if action_prop is None:
        return -1
    else:
        for act_prop in action_prop:
            name = act_prop.get("name")
            assert name is not None, "Missing name"
            icon_prop = act_prop.get("icon")
            icon = create_icon(icon_prop=icon_prop, 
                               main_path=main_path)
            action = QAction(name, self)
            action.setIcon(icon)
            tooltip = act_prop.get("tooltip")
            if tooltip is not None:
                action.setToolTip(tooltip)
            visible = act_prop.get("visible")
            switchers = {
                "TrailingPosition": self.TrailingPosition,
                "LeadingPosition": self.LeadingPosition,
            }
            position = act_prop.get("position")
            self.addAction(action, switchers.get(position))
            if visible is not None:
                action.setVisible(visible)
        return 0


def create_icon(icon_prop, main_path):
    if icon_prop is None:
        return None
    else:
        icon_path = icon_prop.get("path")
        if icon_path is None:
            return None
        else:
            pixmap = QPixmap(os.path.abspath(os.path.join(main_path, icon_path)))
            icon_size = icon_prop.get("size")
            if icon_size is None:
                icon = QIcon(pixmap)
            else:
                icon = QIcon(pixmap.scaled(icon_size[0], icon_size[1]))
            return icon


def setup_date(self, date_str, minimum_date_str, maximum_date_str):
    if self.__class__ in [QDateEdit]:
        self.setDate(QDate.currentDate())
        date = QDate.fromString(date_str, "dd-MM-yyyy")
        minimum_date = QDate.fromString(minimum_date_str, "dd-MM-yyyy")
        maximum_date = QDate.fromString(maximum_date_str, "dd-MM-yyyy")
        self.setMinimumDate(minimum_date)
        self.setMaximumDate(maximum_date)
        self.setDate(date)
        return 0
    else:
        return -1


def get_date_from_String(date_str):
    if date_str is not None:
        date_list = date_str.split('-')
        assert len(date_list) == 3, "Invalid minimum date"
        minimum_date = QDate(int(date_list[2]),
                             int(date_list[1]),
                             int(date_list[0]))
    else:
        minimum_date = None
    return minimum_date


def setup_callback(self, callback_prop: dict, GUI):
    if callback_prop is None:
        return -1
    else:
        assert isinstance(callback_prop, dict), "Invalid callback"
        self.installEventFilter(GUI)
        mouse_event = MouseEvent(obj=self)
        for name, event_prop in callback_prop.items():
            rect = event_prop.get("rect")
            assert isinstance(rect, dict), "Rect is invalid"
            task = event_prop.get("task")
            assert isinstance(task, str) and len(
                task) > 0, "Task name is invalid"
            event = event_prop.get("event")
            assert isinstance(event, str), "event is invalid"
            mouse_event.add_event(name=name,
                                  event=event,
                                  task=task,
                                  rect=rect)


def setup_document(self, document: dict):
    if document is None:
        return -1
    else:
        CLASS = self.__class__
        if CLASS in [QGraphicsTextItem]:
            multi_text = document.get("multi_text")
            assert isinstance(multi_text, list), "Invalid format"
            para = " ".join(multi_text)
            fmt_str = document.get("format")
            text_document = self.document()
            scale = document.get("scale")

            switchers = {
                "PlainText": text_document.setPlainText,
                "RichText": text_document.setHtml,
                "MarkdownText": text_document.setMarkdown,
            }
            FUNCTION = switchers.get(fmt_str)
            if FUNCTION is None:
                return -1
            else:
                return FUNCTION(para)
        else:
            return -1


def childConfig_lambda(self):
    return lambda child_prop, GUI, main_path: childConfig(self,
                                               child_prop,
                                               GUI,
                                               main_path)


def setup_grid_lambda(self):
    return lambda obj, grid_prop: setup_grid(self,
                                             obj,
                                             grid_prop)


def create_object_lambda(self):
    return lambda cls, name: create_object(self,
                                           cls,
                                           name)


def create_named_object_lambda(self):
    return lambda cls, name: create_named_object(self,
                                                 cls,
                                                 name)


def create_nameless_object_lambda(self):
    return lambda cls, name: create_nameless_object(self,
                                                    cls,
                                                    name)


def setup_pos_size_lambda(self):
    return lambda obj, position_prop, size_prop: setup_pos_size(self,
                                                                obj,
                                                                position_prop,
                                                                size_prop)


def setup_action_lambda(self):
    return lambda action_prop, main_path: setup_action(self,
                                                       action_prop,
                                                       main_path)


def setup_date_lambda(self):
    return lambda date_str, minimum_date_str, maximum_date_str: setup_date(self,
                                                                           date_str,
                                                                           minimum_date_str,
                                                                           maximum_date_str)


def setup_callback_lambda(self):
    return lambda callback_prop, GUI: setup_callback(self,
                                                     callback_prop,
                                                     GUI)


def setup_document_lambda(self):
    return lambda document: setup_document(self,
                                           document)
