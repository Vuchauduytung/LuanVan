from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.sip import *
from pyqt_support import *
from task import *
from method_support import *


class MouseEvent:

    event: dict = {}

    def __init__(self, obj):
        self.event: dict = {}
        self.obj = obj
        if obj not in MouseEvent.event.keys():
            MouseEvent.event[obj] = self

    def add_event(self, name: str, event_type: str, button: Qt.MouseButton, rect: QRect, condition, task):
        if name not in self.event.keys():
            self.event[name] = {
                "type": event_type,
                "button": button,
                "rect": rect,
                "condition": condition,
                "task": task
            }

    @classmethod
    def mousePressEvent(cls, UI: QMainWindow, event: QMouseEvent):
        if event.__class__ in [QGraphicsSceneMouseEvent]:
            pos = event.scenePos()
        else:
            pos = event.pos()
        button_event = event.button()
        for _, object_events in cls.event.items():
            for _, event_prop in object_events.event.items():
                TYPE = event_prop.get("type")
                if TYPE == "mouseClick":
                    rect = event_prop.get("rect")
                    button = event_prop.get("button")
                    condition = event_prop.get("condition")
                    if MethodSupport.pos_in_rect(rect, pos) and button == button_event and condition(UI):
                        task = event_prop.get("task")
                        task(UI)

    @classmethod
    def mouseReleaseEvent(cls, UI: QMainWindow, event: QMouseEvent):
        pos = event.pos()
        button_event = event.button()
        for _, object_events in cls.event.items():
            for _, event_prop in object_events.event.items():
                TYPE = event_prop.get("type")
                if TYPE == "mouseRelease":
                    rect = event_prop.get("rect")
                    button = event_prop.get("button")
                    condition = event_prop.get("condition")
                    if not MethodSupport.pos_in_rect(rect, pos) and button == button_event and condition(UI):
                        task = event_prop.get("task")
                        task(UI)

    @classmethod
    def mouseMoveEvent(cls, UI: QMainWindow, event: QMouseEvent):
        pos = event.scenePos()
        for _, object_events in cls.event.items():
            for _, event_prop in object_events.event.items():
                TYPE = event_prop.get("type")
                rect = event_prop.get("rect")
                condition = event_prop.get("condition")
                if TYPE == "mouseOver" and MethodSupport.pos_in_rect(rect, pos) and condition(UI):
                    task = event_prop.get("task")
                elif TYPE == "mouseLeave" and not MethodSupport.pos_in_rect(rect, pos) and condition(UI):
                    task = event_prop.get("task")
                else:
                    task = None
                if task is not None:
                    task(UI)

    def setup_mouse_event(self, UI: QMainWindow):
        self.obj.mousePressEvent = lambda event: MouseEvent.mousePressEvent(
            UI, event)
        self.obj.mouseReleaseEvent = lambda event: MouseEvent.mouseReleaseEvent(
            UI, event)
        self.obj.mouseMoveEvent = lambda event: MouseEvent.mouseMoveEvent(
            UI, event)
