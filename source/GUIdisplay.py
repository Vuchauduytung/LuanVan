from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from modules.library.IO_support import *

class Ui(QtWidgets.QMainWindow):
    """
    Application
    """

    def __init__(self, main_path):
        super(Ui, self).__init__()
        self.main_path = main_path
        # load GUI
        gui_path = os.path.abspath(
            os.path.join(main_path, "GUI", "GUIdisplay.ui"))
        uic.loadUi(gui_path, self)
        self.setup_pushButton()
        #self.setup_lineEdit()
        self.show()
        
    def setup_lineEdit(self):
        GB_information_custom: QGroupBox = self.findChild(QGroupBox, "GB_information_custom")
        LE_name: QLineEdit = self.findChild(QLineEdit, "LE_name")
        LE_Comp_temp_C: QLineEdit = self.findChild(QLineEdit, "LE_Comp_temp_C")
        LE_Comp_temp_F: QLineEdit = self.findChild(QLineEdit, "LE_Comp_temp_F")
        LE_watt: QLineEdit = self.findChild(QLineEdit, "LE_watt")
        LE_name.setText(value_LE_name)
        LE_Comp_temp_C.setText(str(round(temperature_C,4)))
        LE_Comp_temp_F.setText(str(round(temperature_F,4)))
        LE_watt.setText(str(round(compression_pressure,4)))
        
    def LE_focusOutEvent(UI, self: QLineEdit, event: QFocusEvent):
        if self.text() == "":
            self.action.setVisible(True)
        else:
            self.action.setVisible(False)
        QLineEdit.focusOutEvent(self, event)
        
    def setup_pushButton(self):
        # GB_informatin_custom QGroupBox
        BT_graph_fix: QPushButton = self.findChild(QPushButton, "BT_graph_fix")
        BT_graph_fix.clicked.connect(self.BT_graph_fix_click)
        
        BT_graph: QPushButton = self.findChild(QPushButton, "BT_graph")
        BT_graph.clicked.connect(self.BT_graph_click)
        
        BT_fix: QPushButton = self.findChild(QPushButton, "BT_fix")
        BT_fix.clicked.connect(self.BT_fix_click)
        
        BT_cancel: QPushButton = self.findChild(QPushButton, "BT_cancel")
        BT_cancel.clicked.connect(self.BT_cancel_click)
        
    def BT_graph_fix_click(self):
        file_data = os.path.abspath(os.path.join(self.main_path, "source", "GUIgraph_fix.py"))
        os.system('python "{}"'.format(file_data))
        
    def BT_graph_click(self):
        file_data = os.path.abspath(os.path.join(self.main_path, "source", "GUIgraph_xylanh.py"))
        os.system('python "{}"'.format(file_data))
        
    def BT_fix_click(self):
        file_data = os.path.abspath(os.path.join(self.main_path, "source","modules","library","Open_pdf.py"))
        os.system('python "{}"'.format(file_data))
        
    def BT_cancel_click(self):
        window.close()
        
    

if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path)
    app.exec_()
