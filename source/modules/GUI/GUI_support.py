from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

a = 1


def ShowWarning(line_edit: QLineEdit, icon_path: str, msg: str):
    icon = QIcon(icon_path)
    action = line_edit.addAction(icon, line_edit.TrailingPosition)
    action.setToolTip(msg)
    return action


def HideWarning(action: QAction):
    action.setVisible(False)


class Items:

    __instance_list: list = []
    __child: list = []

    @classmethod
    def cast(cls, instance, name: str):
        """Cast an some instance into a this class object."""
        assert (instance.__class__ in cls.__bases__), "Instance {instance}'s class should in {base_classes} object."\
            .format(instance=instance,
                    base_classes=cls.__bases__)
        instance.__class__ = cls  # now mymethod() is available
        assert isinstance(instance, cls), "Cast from class {class_1} to {class_2} unsuccessful."\
            .format(class_1=instance.__class__,
                    class_2=cls)
        instance.name = name
        cls.update_instance_list(instance=instance)
        return instance

    @classmethod
    def update_instance_list(cls, instance):
        name = instance.name
        class_ = cls.__name__
        assert cls.get_instance(name=name) is None, "Duplicate instance name '{name}' in class {class_}."\
            .format(name=name,
                    class_=class_)
        cls.__instance_list += [instance]         
            
    @classmethod
    def get_instance(cls, name: str):
        for ins in cls.__instance_list:
            if ins.name == name:
                ret_ins = ins
                break
        else:
            ret_ins = None
        return ret_ins
    
    @classmethod
    def get_instance_list(cls) -> tuple:
        return tuple(cls.__instance_list)
            

    def __init__(self):
        self.__child: list = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, ins_name: str):
        assert isinstance(ins_name, str), "Instance's name must be string."
        self.__name = ins_name

    @property
    def child(self) -> tuple:
        return tuple(self.__child)

    @child.setter
    def child(self, instance_list):
        for ins in instance_list:
            name = ins.name
            class_ = type(ins)
            assert self.get_child(typ=class_,
                                  name=name) is None\
                                      , "Duplicate name '{name}'.".format(name=name)
            self.__child += [ins]
                
    def get_child(self, typ, name: str):
        for child in self.__child:
            if child.name == name and child.__class__ == typ:
                ret_child = child
                break
        else:
            ret_child = None
        return ret_child
            
