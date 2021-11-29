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
        if self.__class__ not in [QGraphicsScene, QGraphicsTextItem, QGraphicsRectItem]:
            self.grid_layout = QGridLayout()
            self.setLayout(self.grid_layout)
        for name, prop in child_prop.items():
            cls_name = prop.get("class")
            CLASS = PyQtSupport.get_class(cls_name=cls_name)
            assert CLASS is not None, "Unregconize class"
            obj = GUI.create_object(cls=CLASS,
                                    name=name,
                                    parent=self)
            obj.common_config = common_config_lambda(obj)
            obj.common_config(prop=prop,
                              main_path=main_path,
                              GUI=GUI)
            self.get_rect = get_rect_lambda(self)
            rect = self.get_rect()
            obj.specific_config = specific_config_lambda(obj)
            obj.specific_config(prop=prop,
                                main_path=main_path,
                                GUI=GUI,
                                parent_rect=rect)
            grid_prop = prop.get("grid")
            self.setup_grid(obj=obj,
                            grid_prop=grid_prop)
        return 0


def common_config(self, prop: dict, main_path: str, GUI: QMainWindow):
    icon_prop = prop.get("icon")
    setup_icon(obj=self,
               icon_prop=icon_prop,
               main_path=main_path)
    geometry_prop = prop.get("geometry")
    setup_geometry(obj=self,
                   geometry_prop=geometry_prop)
    font_prop = prop.get("font")
    setup_font(obj=self,
               font_prop=font_prop)
    text = prop.get("text")
    format_str = prop.get("format")
    setup_text(obj=self,
               text=text,
               format_str=format_str)
    visible = prop.get("visible")
    setup_visible(obj=self,
                  visible=visible)
    position_prop = prop.get("position")
    size_prop = prop.get("size")
    self.setup_pos_size = setup_pos_size_lambda(self)
    self.setup_pos_size(obj=self,
                        position_prop=position_prop,
                        size_prop=size_prop)
    callback_prop = prop.get("callback")
    self.setup_callback = setup_callback_lambda(self)
    self.setup_callback(callback_prop=callback_prop,
                        GUI=GUI)
    self.childConfig = childConfig_lambda(self)
    self.childConfig(child_prop=prop.get("children"),
                     GUI=GUI,
                     main_path=main_path)


def specific_config(self, prop: dict, main_path: str, GUI: QMainWindow, parent_rect: float):
    if self.__class__ in [QLineEdit]:
        action_prop = prop.get("action")
        self.setup_action = setup_action_lambda(self)
        self.setup_action(action_prop=action_prop,
                          main_path=main_path,
                          UI=GUI)
    elif self.__class__ in [QDateEdit]:
        date = prop.get("date")
        minimum_date = prop.get("minimum_date")
        maximum_date = prop.get("maximum_date")
        self.setup_date = setup_date_lambda(self)
        self.setup_date(date_str=date,
                        minimum_date_str=minimum_date,
                        maximum_date_str=maximum_date)
    elif self.__class__ in [QGraphicsTextItem]:
        document = prop.get("document")
        self.setup_document = setup_document_lambda(self)
        self.setup_document(document=document)
        scale = prop.get("scale")
        self.setup_scale = setup_scale_lambda(self)
        self.setup_scale(scale=scale,
                         parent_rect=parent_rect)
    elif self.__class__ in [QGraphicsRectItem]:
        brush_prop = prop.get("brush")
        pen_prop = prop.get("pen")
        self.setup_brush = setup_brush_lambda(self)
        self.setup_brush(brush_prop=brush_prop)
        self.setup_pen = setup_pen_lambda(self)
        self.setup_pen(pen_prop=pen_prop)
        scale = prop.get("scale")
        self.setup_scale = setup_scale_lambda(self)
        self.setup_scale(scale=scale,
                         parent_rect=parent_rect)


def create_object(self, cls, name: str, parent):
    obj = self.findChild(cls, name)
    if obj is not None:
        return obj
    else:
        return PyQtSupport.create_object(UI=self,
                                         CLASS=cls,
                                         name=name,
                                         parent=parent)


def get_object(self: QMainWindow, cls_name: str, name: str):
    CLASS = PyQtSupport.get_class(cls_name=cls_name)
    if CLASS is None or name is None:
        return None
    else:
        return PyQtSupport.get_object(UI=self, 
                                      CLASS=CLASS, 
                                      name=name)


def setup_icon(obj, icon_prop: dict, main_path: str):
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


def setup_geometry(obj, geometry_prop: dict):
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


def setup_font(obj, font_prop: dict):
    if font_prop is None:
        return -1
    else:
        fam = font_prop.get("family") or obj.font().defaultFamily()
        psz = font_prop.get("pointSize") or -1
        w = font_prop.get("weight") or -1
        itl = font_prop.get("italic") or False
        return PyQtSupport.set_font(obj=obj,
                                    fam=fam,
                                    psz=psz,
                                    w=w,
                                    itl=itl)


def setup_text(obj, text: str, format_str: str):
    if text is None:
        return -1
    else:
        return PyQtSupport.set_text(obj=obj,
                                    text=text,
                                    format_str=format_str)


def setup_grid(self, obj, grid_prop: dict):
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
        ]) != None) and obj.__class__ not in [QGraphicsScene, QGraphicsTextItem, QGraphicsRectItem]:
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


def setup_visible(obj, visible: bool):
    if visible is None:
        return -1
    else:
        return PyQtSupport.set_visible(obj=obj,
                                       visible=visible)


def setup_pos_size(self, obj, position_prop: dict, size_prop: dict):
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


def create_icon(icon_prop: dict, main_path: str):
    if icon_prop is None:
        return None
    else:
        icon_path = icon_prop.get("path")
        if icon_path is None:
            return None
        else:
            pixmap = QPixmap(os.path.abspath(
                os.path.join(main_path, icon_path)))
            icon_size = icon_prop.get("size")
            if icon_size is None:
                icon = QIcon(pixmap)
            else:
                icon = QIcon(pixmap.scaled(icon_size[0], icon_size[1]))
            return icon


def setup_date(self: QDateEdit, date_str: str, minimum_date_str: str, maximum_date_str: str):
    self.setDate(QDate.currentDate())
    date = QDate.fromString(date_str, "dd-MM-yyyy")
    minimum_date = QDate.fromString(minimum_date_str, "dd-MM-yyyy")
    maximum_date = QDate.fromString(maximum_date_str, "dd-MM-yyyy")
    self.setMinimumDate(minimum_date)
    self.setMaximumDate(maximum_date)
    self.setDate(date)


def setup_callback(self, callback_prop: dict, GUI: QMainWindow):
    if callback_prop is None:
        return -1
    else:
        assert isinstance(callback_prop, dict), "Invalid callback"
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
        event_prop: dict
        for event_prop in mouse_event_prop:
            rect_prop = event_prop.get("rect")
            rect = MethodSupport.create_rect(rect_prop=rect_prop)
            task_prop: dict = event_prop.get("task")
            event_type = event_prop.get("event")
            button_name = event_prop.get("button")
            button = MethodSupport.get_button(button_name=button_name)
            for task_name, condition_name in task_prop.items():
                TASK = MethodSupport.get_task(task_name=task_name)
                assert TASK, "undefined mouse event, task '{task_name}'"\
                    .format(task_name=task_name)
                CONDITION = MethodSupport.get_condition(
                    condition_name=condition_name)
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
        event_prop: dict
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
            task_prop: dict = event_prop.get("task")
            task_dict = {}
            for task_name, condition_name in task_prop.items():
                TASK = MethodSupport.get_task(task_name=task_name)
                assert TASK, "invalid button event, task {task_name}"\
                    .format(task_name=task_name)
                CONDITION = MethodSupport.get_condition(
                    condition_name=condition_name)
                assert CONDITION, "undefined mouse event, condition {condition_name}"\
                    .format(condition_name=condition_name)
                task_dict.update({
                    CONDITION: TASK
                })
            FUNCTION.connect(lambda: MethodSupport.run_task(task_dict,
                                                            UI))
        return 0


def setup_document(self: QGraphicsTextItem, document: dict):
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


def setup_brush(self: QGraphicsRectItem, brush_prop: dict):
    if brush_prop is None:
        return -1
    else:
        color_val = brush_prop.get('color')
        color = MethodSupport.create_color(color_val=color_val)
        brush = QBrush(color)
        brush.setColor(color)
        self.setBrush(brush)
        return 0


def setup_pen(self: QGraphicsRectItem, pen_prop: dict):
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
        assert isinstance(width, float) or isinstance(
            width, int), "width must be a number"
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
    return lambda cls_name, name: get_object(self,
                                             cls_name,
                                             name)


def common_config_lambda(self):
    return lambda prop, main_path, GUI: common_config(self,
                                                      prop,
                                                      main_path,
                                                      GUI)


def specific_config_lambda(self):
    return lambda prop, main_path, GUI, parent_rect: specific_config(self,
                                                                     prop,
                                                                     main_path,
                                                                     GUI,
                                                                     parent_rect)
