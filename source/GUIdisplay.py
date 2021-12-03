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
        self.show()
        
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
        window.close()
        
    def BT_fix_click(self):
        window.close()
        
    def BT_cancel_click(self):
        window.close()
        
    

if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path)
    app.exec_()
