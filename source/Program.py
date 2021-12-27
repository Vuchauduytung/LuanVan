from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
# Import json module
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
            os.path.join(main_path, "GUI", "Program.ui"))
        uic.loadUi(gui_path, self)
        self.setup_pushButton_cus()
        self.setup_pushButton_search()
        self.icon()
        self.show()

    def icon(self):
        self.setWindowIcon(QIcon('source\icon\Logo BK.png'))
        
    def setup_pushButton_cus(self):
        # GB_informatin_custom QGroupBox
        BT_search: QPushButton = self.findChild(QPushButton, "BT_custom_new")
        BT_search.clicked.connect(self.custom_new)
        
    def setup_pushButton_search(self):
        # GB_informatin_custom QGroupBox
        BT_cancel: QPushButton = self.findChild(QPushButton, "BT_search_custom")
        BT_cancel.clicked.connect(self.search_custom)
                    
    def custom_new(self):
        path = os.path.abspath(os.path.dirname(__file__))
        main_path = os.path.abspath(os.path.join(path, os.pardir))
        direct_path = os.path.abspath(os.path.join(main_path, "source", "GUIinput.py"))
        os.system("python3 \"{path}\""\
            .format(path=direct_path))
        
    def search_custom(self):
        path = os.path.abspath(os.path.dirname(__file__))
        main_path = os.path.abspath(os.path.join(path, os.pardir))
        direct_path = os.path.abspath(os.path.join(main_path, "source", "GUIsearch.py"))
        os.system("python3 \"{path}\""\
            .format(path=direct_path))
        
        
        
if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path)
    app.exec_()

