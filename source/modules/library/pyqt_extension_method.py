from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import numpy as np
from IO_support import *
from pyqt_support import *
from pyqt_event import *
from method_support import *
from task import *

def childConfig(self, child_prop: dict, GUI: QMainWindow, main_path: str):
    if child_prop is None:
        return -1
    else:
        assert isinstance(child_prop, dict), "'child' must be in dict type"
        self.nameless_child = {}
        self.setup_grid = setup_grid_lambda(self)
        for name, prop in child_prop.items():
            class_str = prop.get("class")
            CLASS = PyQtSupport.get_class(class_str=class_str)
            assert CLASS is not None, "Unregconize class"

            obj = GUI.create_object(cls=CLASS,
                                    name=name,
                                    parent=self)

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
                             main_path=main_path,
                             UI=GUI)
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
            self.get_rect = get_rect_lambda(self)
            parent_rect = self.get_rect()
            scale = prop.get("scale")
            obj.setup_scale = setup_scale_lambda(obj)
            obj.setup_scale(scale=scale,
                            parent_rect=parent_rect)
            obj.setup_date = setup_date_lambda(obj)
            obj.setup_date(date_str=date,
                           minimum_date_str=minimum_date,
                           maximum_date_str=maximum_date)
            brush_prop = prop.get("brush")
            pen_prop = prop.get("pen")
            obj.setup_brush = setup_brush_lambda(obj)
            obj.setup_brush(brush_prop=brush_prop)
            obj.setup_pen = setup_pen_lambda(obj)
            obj.setup_pen(pen_prop=pen_prop)

            if obj.__class__ not in [QGraphicsScene, QGraphicsTextItem, QGraphicsRectItem]:
                obj.grid_layout = QGridLayout()
                obj.setLayout(obj.grid_layout)
            obj.childConfig = childConfig_lambda(obj)
            obj.childConfig(child_prop=prop.get("children"),
                            GUI=GUI,
                            main_path=main_path)
        return 0

# def common_config(self, child_prop: dict, GUI: QMainWindow, main_path: str):

def create_object(self, cls, name, parent):
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
        return self.create_obj(cls,
                               name,
                               parent)


def create_named_object(self, cls, name, _):
    obj = cls(self)
    obj.setAccessibleName(name)
    return obj


def create_nameless_object(self, cls, name, parent):
    switchers = {
        QGraphicsScene: True,
        QGraphicsTextItem: False,
        QGraphicsRectItem: False,
        QAction: True
    }
    heritage = switchers.get(cls)
    # TYPE = choice[0]
    # heritage = choice[1]
    if heritage:
        obj = cls(self)
        if obj.__class__ in [QGraphicsScene]:
            parent.setScene(obj)
    else:
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
    if cls in self.nameless_child.keys():
        self.nameless_child[cls].update({
            name: obj
        })
    else:
        self.nameless_child[cls] = {
            name: obj
        }
    return obj

def get_object(self: QMainWindow, class_str, name: str):
    CLASS = PyQtSupport.get_class(class_str=class_str)
    if CLASS is None or name is None:
        return None
    else:
        switchers = {
            QLabel: lambda CLASS, name: self.findChild(CLASS, name),
            QLineEdit: lambda CLASS, name: self.findChild(CLASS, name),
            QGroupBox: lambda CLASS, name: self.findChild(CLASS, name),
            QPushButton: lambda CLASS, name: self.findChild(CLASS, name),
            QCheckBox: lambda CLASS, name: self.findChild(CLASS, name),
            QGraphicsView: lambda CLASS, name: self.findChild(CLASS, name),
            QGraphicsScene: lambda CLASS, name: self.nameless_child.get(CLASS).get(name),
            QGraphicsTextItem: lambda CLASS, name: self.nameless_child.get(CLASS).get(name),
            QGraphicsRectItem: lambda CLASS, name: self.nameless_child.get(CLASS).get(name),
            QAction: lambda CLASS, name: self.nameless_child.get(CLASS).get(name),
            QDateEdit: lambda CLASS, name: self.findChild(CLASS, name)
        }
        FUNCTION = switchers.get(CLASS)
        if FUNCTION is None:
            return None
        else:
            return FUNCTION(CLASS=CLASS,
                            name=name)



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


def setup_action(self, action_prop: dict, main_path: str, UI: QMainWindow):
    if action_prop is None:
        return -1
    else:
        for act_prop in action_prop:
            name = act_prop.get("name")
            assert name is not None, "Missing name"
            icon_prop = act_prop.get("icon")
            icon = create_icon(icon_prop=icon_prop, 
                               main_path=main_path)
            action = UI.create_object(cls=QAction, 
                                      name=name, 
                                      parent=None)
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


def setup_callback(self, callback_prop: dict, GUI: QMainWindow):
    if callback_prop is None:
        return -1
    else:
        assert isinstance(callback_prop, dict), "Invalid callback"
        # self.installEventFilter(GUI)
        mouse_event_prop = callback_prop.get("mouse_event")
        setup_mouse_event(self, 
                          mouse_event_prop,
                          GUI)
        button_event_prop = callback_prop.get("button_event")
        setup_button_event(self,
                           button_event_prop,
                           GUI)
        return 0
          
def setup_mouse_event(self, mouse_event_prop: dict, GUI: QMainWindow):
    if mouse_event_prop is None:
        return -1
    else:
        mouse_event = MouseEvent(obj=self)
        for event_prop in mouse_event_prop:
            rect_prop = event_prop.get("rect")
            rect = MethodSupport.create_rect(rect_prop=rect_prop)
            # assert isinstance(rect, dict), "Rect is invalid"
            task_prop = event_prop.get("task")
            event_type = event_prop.get("event")
            button_name = event_prop.get("button")
            button = MethodSupport.get_button(button_name=button_name)
            for task_name, condition_name in task_prop.items():
                TASK = MethodSupport.get_task(task_name=task_name)
                assert TASK, "undefined mouse event, task '{task_name}'"\
                    .format(task_name=task_name)
                CONDITION = MethodSupport.get_condition(condition_name=condition_name)
                assert CONDITION, "undefined mouse event, condition '{condition_name}'"\
                    .format(condition_name=condition_name)     
                mouse_event.add_event(name=task_name,
                                      event_type=event_type,
                                      button=button,
                                      rect=rect,
                                      condition=CONDITION,
                                      task=TASK)
        mouse_event.setup_mouse_event(UI=GUI)
        return 0
    
def setup_button_event(self, button_event_prop: dict, UI: QMainWindow):
    if button_event_prop is None:
        return -1
    else:
        for event_prop in button_event_prop:
            event = event_prop.get("event")
            switchers = {
                "clicked": self.clicked,
                "pressed": self.pressed,
                "released": self.released,
                "toggled": self.toggled
            }
            FUNCTION = switchers.get(event)
            assert FUNCTION, "Invalid button event"
            task_prop = event_prop.get("task")
            task_dict = {}
            for task_name, condition_name in task_prop.items():
                TASK = MethodSupport.get_task(task_name=task_name)
                assert TASK, "invalid button event, task {task_name}"\
                    .format(task_name=task_name)
                CONDITION = MethodSupport.get_condition(condition_name=condition_name)
                assert CONDITION, "undefined mouse event, condition {condition_name}"\
                    .format(condition_name=condition_name)
                task_dict.update({
                    CONDITION: TASK
                })
                
            FUNCTION.connect(lambda: MethodSupport.run_task(task_dict,
                                                            UI))
        return 0

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
        
def get_rect(self):
    return PyQtSupport.get_rect(self)
    
        
def setup_scale(self, scale: float, parent_rect: tuple):
    if scale is None:
        return -1
    else:
        assert isinstance(scale, float), "scale must be a float number"
        return PyQtSupport.set_scale(obj=self, 
                                     parent_rect=parent_rect, 
                                     scale=scale)
        
def setup_brush(self, brush_prop: dict):
    if brush_prop is None:
        return -1 
    else:
        color_val = brush_prop.get('color')
        color = MethodSupport.create_color(color_val=color_val)
        brush = QBrush(color)
        brush.setColor(color)
        self.setBrush(brush)
        return 0
    
def setup_pen(self, pen_prop: dict):
    if pen_prop is None:
        return -1
    else:
        color_val = pen_prop.get('color')
        color = MethodSupport.create_color(color_val=color_val)
        style_prop = pen_prop.get('style')
        switchers = {
            "NoPen": Qt.PenStyle.NoPen,
            "SolidLine": Qt.PenStyle.SolidLine,
            "DashLine": Qt.PenStyle.DashLine,
            "DotLine": Qt.PenStyle.DotLine,
            "DashDotLine": Qt.PenStyle.DashDotLine,
            "DashDotDotLine": Qt.PenStyle.DashDotDotLine,
        }
        style = switchers.get(style_prop)
        width = pen_prop.get('width')
        assert isinstance(width, float) or isinstance(width, int), "width must be a number"
        pen = QPen()
        pen.setColor(color)
        pen.setStyle(style)
        pen.setWidth(width)
        self.setPen(pen)
        return 0

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
    return lambda cls, name, parent: create_object(self,
                                           cls,
                                           name,
                                           parent)


def create_named_object_lambda(self):
    return lambda cls, name, parent: create_named_object(self,
                                                 cls,
                                                 name,
                                                 parent)


def create_nameless_object_lambda(self):
    return lambda cls, name, parent: create_nameless_object(self,
                                                            cls,
                                                            name,
                                                            parent)


def setup_pos_size_lambda(self):
    return lambda obj, position_prop, size_prop: setup_pos_size(self,
                                                                obj,
                                                                position_prop,
                                                                size_prop)


def setup_action_lambda(self):
    return lambda action_prop, main_path, UI: setup_action(self,
                                                       action_prop,
                                                       main_path,
                                                       UI)


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
    
def setup_scale_lambda(self):
    return lambda scale, parent_rect: setup_scale(self, 
                                                  scale, 
                                                  parent_rect)

def get_rect_lambda(self):
    return lambda: get_rect(self)

def setup_brush_lambda(self):
    return lambda brush_prop: setup_brush(self, 
                                          brush_prop)

def setup_pen_lambda(self):
    return lambda pen_prop: setup_pen(self, 
                                      pen_prop)

def get_object_lambda(self):
    return lambda class_str, name: get_object(self, 
                                              class_str, 
                                              name)