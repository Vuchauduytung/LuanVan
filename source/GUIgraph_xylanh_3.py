from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from modules.library.IO_support import *
from modules.library.pyqt_support import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class Ui(QtWidgets.QMainWindow):
    """
    Application
    """

    def __init__(self, main_path):
        super(Ui, self).__init__()
        self.main_path = main_path
        # load GUI
        gui_path = os.path.abspath(
            os.path.join(main_path, "GUI", "GUIgraph_xylanh3.ui"))
        uic.loadUi(gui_path, self)
        self.setup_pushButton()
        self.setup_graph()
        self.show()
    # Hien do thi giong GUI main
    def setup_graph(self):
        GV_graph: QGraphicsView = self.findChild(QGraphicsView, "GV_graph")
        data_path = os.path.abspath(os.path.join(self.main_path,"Mô phỏng Matlab", "data" ,"data_P_xylanh3.json"))
        customer = json2dict(data_path)
        graph = customer["Data"]
        # Tinh tong gia tri trong json
        k = int(len(graph))
        # Tao list
        data_list_time = list(range(0,k))
        data_list_P = list(range(0,k))
        i = 0
        for graph[i] in graph:
            data_list_time[i] =  customer["Data"][i]['time']
            data_list_P[i] =  customer["Data"][i]['pmin_1']
            i+=1
        # Ve do thi ap suat nen   
        self.scene = QtWidgets.QGraphicsScene(self.GV_graph)
        self.GV_graph.setScene(self.scene)
        figure = Figure()
        axes = figure.gca()
        axes.set_title("Do thi ap suat nen")
        axes.plot(data_list_time, data_list_P, "-k", label="Ap suat ")
        axes.legend()
        axes.grid(True)
        canvas = FigureCanvas(figure)
        proxy_widget = self.scene.addWidget(canvas)
        proxy_widget = QtWidgets.QGraphicsProxyWidget()
        proxy_widget.setWidget(canvas)
        self.scene.addItem(proxy_widget)
        
    def setup_pushButton(self):
        # GB_informatin_custom QGroupBox
        BT_exit: QPushButton = self.findChild(QPushButton, "BT_exit")
        BT_exit.clicked.connect(self.BT_quit_click)
        
    def BT_quit_click(self):
        window.close()
        
    

if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path)
    app.exec_()
