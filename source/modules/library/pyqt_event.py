from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.sip import *
from pyqt_support import *
from task import *
from method_support import *


# class MouseEvent:
#     """
#     Class này hỗ trợ các tác vụ liên quan đến thao tác chuột.
#     """
#     obj: dict = {}

#     def __init__(self, obj):
#         if obj not in MouseEvent.obj.keys():
#             self.obj = obj
#             self.event = {}
#             MouseEvent.obj = {
#                 obj: self
#             }

#     def add_event(self, name: str, event: str, task, rect: dict):
#         self.event = {
#             name: {
#                 "event": event,
#                 "rect": rect,
#                 "task": task
#             }
#         }

#     @staticmethod
#     def check_position(point: QPointF, rect: dict):
#         if rect.get("x") <= point.x() <= rect.get("x") + rect.get("w")\
#                 and rect.get("y") <= point.y() <= rect.get("y") + rect.get("h"):
#             return True
#         else:
#             return False

#     @classmethod
#     def check_event(cls, e, event, CLASS):
#         return event.type() == cls.get_event(CLASS).get(e)

#     @staticmethod
#     def get_event(CLASS):
#         switchers = {
#             QWidget: {
#                 "mouseOver": QEvent.Enter,
#                 "mouseLeave": QEvent.Leave,
#                 "mouseClick": QEvent.MouseButtonPress,
#                 "mouseRelease": QEvent.MouseButtonRelease
#             },
#             QObject: {
#                 "mouseOver": QEvent.GraphicsSceneHoverMove,
#                 "mouseLeave": QEvent.GraphicsSceneHoverLeave,
#                 "mouseClick": QEvent.GraphicsSceneMousePress,
#                 "mouseRelease": QEvent.GraphicsSceneMouseRelease
#             }
#         }
#         return PyQtSupport.get_value_from_base_class(CLASS=CLASS,
#                                                      sw=switchers)

#     @classmethod
#     def run(cls, obj, event: str, point: QPointF):
#         mouse_event = cls.obj.get(obj)
#         for _, object_events in mouse_event.event.items():
#             rect = object_events.get("rect")
#             con_1 = cls.check_position(point, rect)
#             e = object_events.get("event")
#             con_2 = cls.check_event(e=e,
#                                     event=event,
#                                     CLASS=obj.__class__)
#             if con_1 and con_2:
#                 task_name = object_events.get("task")
#                 result = Task.run_task(task_name=task_name)
#         else:
#             result = False
#         return result
        
        
class MouseEvent:
    
    event: dict = {}
    
    def __init__(self, obj):
        self.event: dict = {}
        self.obj = obj
        if obj not in MouseEvent.event.keys():
            MouseEvent.event[obj] = self
        
    def add_event(self, name: str, event_type: str, button: Qt.MouseButton, rect: QRect, task: str):
        if name not in self.event.keys():
            self.event[name] = {
                "type": event_type,
                "button": button,
                "rect": rect,
                "task": task
            }
            
    @classmethod
    def mousePressEvent(cls, UI: QMainWindow, event: QMouseEvent):
        pos = event.windowPos()
        button_event = event.button()
        for _, object_events in cls.event.items():
            for _, event_prop in object_events.event.items():
                TYPE = event_prop.get("type")
                if TYPE == "mouseClick":
                    rect = event_prop.get("rect")
                    button = event_prop.get("button")
                    if MethodSupport.pos_in_rect(rect, pos) and button == button_event:
                        task = event_prop.get("task")
                        task(UI)
                
    @classmethod
    def mouseReleaseEvent(cls, UI: QMainWindow, event: QMouseEvent):
        pos = event.windowPos()
        button_event = event.button()
        for _, object_events in cls.event.items():
            for _, event_prop in object_events.event.items():
                TYPE = event_prop.get("type")
                if TYPE == "mouseRelease":
                    rect = event_prop.get("rect")
                    button = event_prop.get("button")
                    if not MethodSupport.pos_in_rect(rect, pos) and button == button_event:
                        task = event_prop.get("task")
                        task(UI)      
                
    @classmethod
    def mouseMoveEvent(cls, UI: QMainWindow, event: QMouseEvent):
        pos = event.screenPos()
        for _, object_events in cls.event.items():
            for _, event_prop in object_events.event.items():
                TYPE = event_prop.get("type")
                rect = event_prop.get("rect")
                if TYPE == "mouseOver" and MethodSupport.pos_in_rect(rect, pos):
                    task = event_prop.get("task")
                    task(UI)    
                elif TYPE == "mouseLeave" and not MethodSupport.pos_in_rect(rect, pos):
                    task = event_prop.get("task")
                    task(UI)   
                

    def setup_mouse_event(self, UI: QMainWindow):
        self.obj.mousePressEvent = lambda event: MouseEvent.mousePressEvent(UI, event)
        self.obj.mouseReleaseEvent = lambda event: MouseEvent.mouseReleaseEvent(UI, event)
        self.obj.mouseMoveEvent = lambda event: MouseEvent.mouseMoveEvent(UI, event)