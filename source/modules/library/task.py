from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqt_support import *


class Task:
    """
    Class này hỗ trợ các hàm được liên kết với các event
    của Application
    """

    @classmethod
    def get_task(cls, task_name):
        switchers = {
            "default": cls.default_task,

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
