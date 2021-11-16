from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqt_support import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Task:
    """
    Class này hỗ trợ các hàm được liên kết với các event
    của Application
    """

    @classmethod
    def get_task(cls, task_name: str):
        switchers = {
            "default": cls.default_task,
            "underlined text": cls.task1,
            "not-underlined text": cls.task2,
            "choose image": cls.task3,
            "save and load next GUI": cls.task4,
            "show warning": cls.task5,
            "exit": cls.task6
        }
        return switchers.get(task_name)

    @classmethod
    def run_task(cls, task_name):
        task = cls.get_task(task_name)
        return task()

    @classmethod
    def default_task(cls, _):
        print("Welcome to default task")
        return True
    
    @classmethod
    def task1(cls, UI: QMainWindow):
        Insert_image_hints_text: QGraphicsTextItem = UI.get_object(class_str="QGraphicsTextItem", name="Insert_image_hints_text")
        document=Insert_image_hints_text.document()
        document.setHtml(
            '''
                <STYLE type="text/css">
                DIV.mypars {
                text-align: center;
                font-size: 20px;
                }
                </STYLE>
                <BODY>
                <DIV class="mypars">
                <br /><br /><br /><br /><br />
                <br /><br /><br /><br />
                <P>Drag image here </P>
                <P>Or <span style="color:blue"> <b><u>choose file<u/></b> </P>
                </DIV>
            '''
        )
        return True
    
    @classmethod
    def task2(cls, UI: QMainWindow):
        Insert_image_hints_text: QGraphicsTextItem = UI.get_object(class_str="QGraphicsTextItem", name="Insert_image_hints_text")
        document=Insert_image_hints_text.document()
        document.setHtml(
            '''
                <STYLE type="text/css">
                DIV.mypars {
                text-align: center;
                font-size: 20px;
                }
                </STYLE>
                <BODY>
                <DIV class="mypars">
                <br /><br /><br /><br /><br />
                <br /><br /><br /><br />
                <P>Drag image here </P>
                <P>Or <span style="color:blue"> <b>choose file</b> </P>
                </DIV>
            '''
        )
        return True
    
    @classmethod
    def task3(cls, UI: QMainWindow):
        filenames,_ = QtWidgets.QFileDialog.getOpenFileNames()
        scene: QGraphicsScene = UI.get_object(class_str="QGraphicsScene", name="scene_incident_images")
        # scene =self.scene
        pos = [0,0]
        for file in filenames:
            img = QtGui.QImage(file)
            img = img.scaled(100,100)
            Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
            a=scene.addItem(Pimax_Item)
            Pimax_Item.setOffset(pos[0], pos[1])
            pos[0] += 105
            # pos[1] += 100
        # graphicsView.fitInView(Pimax_Item)
    
    @classmethod
    def task4(cls, UI: QMainWindow):
        action_names = [
            "missing_value_warning_1",
            "missing_value_warning_2",
            "missing_value_warning_3",
            "missing_value_warning_4",
            "missing_value_warning_5"
        ]
        for action_nam in action_names:
            action = UI.get_object(class_str="QAction", name=action_nam)
            action.setVisible(False)
    
    @classmethod
    def task5(cls, UI: QMainWindow):
        action_names = [
            "missing_value_warning_1",
            "missing_value_warning_2",
            "missing_value_warning_3",
            "missing_value_warning_4",
            "missing_value_warning_5"
        ]
        for action_nam in action_names:
            action = UI.get_object(class_str="QAction", name=action_nam)
            action.setVisible(True)
        
    @classmethod
    def task6(cls, UI: QMainWindow):
        UI.close()
        

class Condition:
    """
    Class này hỗ trợ các hàm dùng để check điều kiện cho task
    """
    
    @classmethod
    def get_condition(cls, condition_name: str):
        switchers = {
            None: (lambda UI: True),
            "full information": cls.cond1,
            "missing infomation": cls.cond2
        }
        return switchers.get(condition_name)

    @classmethod
    def cond1(cls, UI: QMainWindow):
        line_edit_1: QLineEdit = UI.get_object(class_str="QLineEdit", name="LE_customer_name")
        line_edit_2: QLineEdit = UI.get_object(class_str="QLineEdit", name="LE_VIN_code")
        line_edit_3: QLineEdit = UI.get_object(class_str="QLineEdit", name="LE_number_plate")
        line_edit_4: QLineEdit = UI.get_object(class_str="QLineEdit", name="LE_phone_number")
        line_edit_5: QLineEdit = UI.get_object(class_str="QLineEdit", name="LE_address")
        if line_edit_1.text() == ""\
            and line_edit_2.text() == ""\
                and line_edit_3.text() == ""\
                    and line_edit_4.text() == ""\
                        and line_edit_5.text() == "":
                            return False
        else:
            return True
    
    @classmethod
    def cond2(cls, UI: QMainWindow):
        return not cls.cond1(UI=UI)