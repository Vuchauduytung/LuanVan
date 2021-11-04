from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqt_support import *
import numpy as np

class MethodSupport:

    @staticmethod
    def create_color(color_val: list):
        assert isinstance(color_val, list) and all([isinstance(e, int) for e in color_val]) and len(color_val) == 3, \
        "invalid color value"
        color = QColor(color_val[0], 
                    color_val[1], 
                    color_val[2])
        return color 

    @staticmethod
    def get_origin(rect: QRect):
        x = rect.x()
        y = rect.y()
        width = rect.width()
        height = rect.height()
        origin = QPointF(x+width/2, y+height/2)
        return origin

    @staticmethod
    def create_rect(rect_prop: QRect):
        x = rect_prop.get("x")
        y = rect_prop.get("y")
        width = rect_prop.get("w")
        height = rect_prop.get("h")
        assert all([isinstance(para, float) or isinstance(para, int) for para in [x, y, width, height]]), \
            "invalid rect"
        return QRect(x, 
                    y, 
                    width, 
                    height)
    
    @staticmethod    
    def get_task(task_name: str):
        assert isinstance(task_name, str) and len(
                    task_name) > 0, "Task name is invalid"
        task = Task.get_task(task_name=task_name)
        return task

    @staticmethod
    def get_button(button_name: str):
        switchers = {
            "LeftButton": Qt.LeftButton,
            "RightButton": Qt.RightButton,
            "MiddleButton": Qt.MiddleButton
        }
        button = switchers.get(button_name)
        return button

    @staticmethod
    def pos_in_rect(rect, pos):
        if pos.x() >= rect.x() and pos.x() <= (rect.x()+ rect.width()) and \
            pos.y() >= rect.y() and pos.y() <= (rect.y()+ rect.height()):
                return True
        else:
            return False