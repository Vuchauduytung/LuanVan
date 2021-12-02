from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os


class Ui(QtWidgets.QMainWindow):
    """
    Application
    """

    def __init__(self, main_path):
        super(Ui, self).__init__()
        self.main_path = main_path
        # load GUI
        gui_path = os.path.abspath(
            os.path.join(main_path, "GUI", "GUIsearch.ui"))
        uic.loadUi(gui_path, self)
        self.setup_lineEdit()
        self.setup_pushButton_search()
        self.setup_pushButton_exit()
        self.show()
        
    def setup_lineEdit(self):
        LE_name_custom: QLineEdit = self.findChild(QLineEdit, "LE_name_custom")
        LE_phone_number: QLineEdit = self.findChild(QLineEdit, "LE_phone_number")
        LE_number_car: QLineEdit = self.findChild(QLineEdit, "LE_number_car")
        icon_path: str = os.path.abspath(os.path.join(
            self.main_path, "source/icon", "exclamation_mark.png"))
        icon = QIcon(icon_path)
        
        LE_name_custom.action = LE_name_custom.addAction(
            icon, LE_name_custom.TrailingPosition)
        LE_phone_number.action = LE_phone_number.addAction(
            icon, LE_phone_number.TrailingPosition)
        LE_number_car.action = LE_number_car.addAction(
            icon, LE_number_car.TrailingPosition)
        
        LE_name_custom.action.setToolTip("Vui lòng nhập tên")
        LE_phone_number.action.setToolTip("Vui lòng nhập số điện thoại")
        LE_number_car.action.setToolTip("Vui lòng nhập biển số")
        
        LE_name_custom.action.setVisible(False)
        LE_phone_number.action.setVisible(False)
        LE_number_car.action.setVisible(False)
        
        LE_name_custom.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_name_custom,
                                                                      event=event)
        LE_phone_number.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_phone_number,
                                                                        event=event)
        LE_number_car.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_number_car,
                                                                      event=event)
        
    def LE_focusOutEvent(UI, self: QLineEdit, event: QFocusEvent):
        if self.text() == "":
            self.action.setVisible(True)
        else:
            self.action.setVisible(False)
        QLineEdit.focusOutEvent(self, event)
        
    def setup_pushButton_search(self):
        # GB_informatin_custom QGroupBox
        BT_search: QPushButton = self.findChild(QPushButton, "BT_search")
        BT_search.clicked.connect(self.BT_search_click)
        
    def setup_pushButton_exit(self):
        # GB_informatin_custom QGroupBox
        BT_exit: QPushButton = self.findChild(QPushButton, "BT_exit")
        BT_exit.clicked.connect(self.BT_quit_click)
        
    def BT_search_click(self):
        window.close()
    
    def BT_quit_click(self):
        window.close()
        
if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path)
    app.exec_()

