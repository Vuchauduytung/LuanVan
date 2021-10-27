from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqt_support import *

class MouseEvent:
    """
    Class này hỗ trợ các tác vụ liên quan đến thao tác chuột.
    """
    obj: dict = {}

    def __init__(self, obj):
        if obj not in MouseEvent.obj.keys():
            self.obj = obj
            self.event = {}
            MouseEvent.obj = {
                obj: self
            }

    def add_event(self, name: str, event: str, task, rect: dict):
        self.event = {
            name: {
                "event": event,
                "rect": rect,
                "task": task
            }
        }

    @staticmethod
    def check_position(point: QPointF, rect: dict):
        if rect.get("x") <= point.x() <= rect.get("x") + rect.get("w")\
                and rect.get("y") <= point.y() <= rect.get("y") + rect.get("h"):
            return True
        else:
            return False

    @classmethod
    def check_event(cls, e, event, CLASS):
        return event.type() == cls.get_event(CLASS).get(e)

    @staticmethod
    def get_event(CLASS):
        switchers = {
            QWidget: {
                "mouseOver": QEvent.Enter,
                "mouseLeave": QEvent.Leave,
                "mouseClick": QEvent.MouseButtonPress,
                "mouseRelease": QEvent.MouseButtonRelease
            },
            QObject: {
                "mouseOver": QEvent.GraphicsSceneHoverMove,
                "mouseLeave": QEvent.GraphicsSceneHoverLeave,
                "mouseClick": QEvent.GraphicsSceneMousePress,
                "mouseRelease": QEvent.GraphicsSceneMouseRelease
            }
        }
        return PyQtSupport.get_value_from_base_class(CLASS=CLASS,
                                                     sw=switchers)

    @classmethod
    def run(cls, obj, event: str, point: QPointF):
        mouse_event = cls.obj.get(obj)
        for _, event_prop in mouse_event.event.items():
            rect = event_prop.get("rect")
            con_1 = cls.check_position(point, rect)
            e = event_prop.get("event")
            con_2 = cls.check_event(e=e,
                                    event=event,
                                    CLASS=obj.__class__)
            if con_1 and con_2:
                task_name = event_prop.get("task")
                result = Task.run_task(task_name=task_name)
        else:
            result = False
        return result
        