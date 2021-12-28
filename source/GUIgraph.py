from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from modules.library.IO_support import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class Ui(QtWidgets.QMainWindow):
    """
    Application
    """

    def __init__(self, main_path: str, phone_number: str, num_xilanh: int):
        super(Ui, self).__init__()
        self.main_path = main_path
        self.phone_number = phone_number
        self.num_xilanh = num_xilanh
        # load GUI
        gui_path = os.path.abspath(
            os.path.join(main_path, "GUI", "GUIgraph.ui"))
        uic.loadUi(gui_path, self)
        self.setWindowTitle("Đồ thị xilanh {num_xilanh}"\
            .format(num_xilanh=self.num_xilanh))
        GB_graph: QGroupBox = self.findChild(QGroupBox, "GB_graph")
        GB_graph.setTitle("Đồ thị xilanh {num_xilanh}"\
            .format(num_xilanh=self.num_xilanh))
        self.get_data()
        self.setup_pushButton()
        self.setup_graph()
        self.icon()
        self.show()

    def get_data(self):
        data_path = os.path.abspath(os.path.join(self.main_path, "data" ,"customers_data.json"))
        customers_list = json2dict(data_path)
        for customer in customers_list:
            if customer.get('phone_number') == self.phone_number:
                break
        else:
            raise Exception("Cannot find customer with phone number \"{phone_number}\""\
                .format(phone_number=self.phone_number))
        self.pres_points = customer.get("Xylanh_{num_xilanh}"\
            .format(num_xilanh=self.num_xilanh))\
                .get("data_points")
        epoch = len(self.pres_points)/720
        self.time_points = np.linspace(start=0, 
                                       stop=epoch*0.5, 
                                       num=len(self.pres_points))
        
    def icon(self):
        self.setWindowIcon(QIcon('source\icon\Logo BK.png'))
    # Hien do thi giong GUI main
    def setup_graph(self):
        GV_graph: QGraphicsView = self.findChild(QGraphicsView, "GV_graph")
        # data_path = os.path.abspath(os.path.join(self.main_path,"matlab_simulator", "data" ,"customers_data.json"))
        # customer = json2dict(data_path)
        # graph = customer["Data"]
        # # Tinh tong gia tri trong json
        # k = int(len(graph))
        # # Tao list
        # data_list_time = list(range(0,k))
        # data_list_P = list(range(0,k))
        # i = 0
        # for graph[i] in graph:
        #     data_list_time[i] =  customer["Data"][i]['time']
        #     data_list_P[i] =  customer["Data"][i]['pmin_1']
        #     i+=1
        # Ve do thi ap suat nen   
        self.scene = QtWidgets.QGraphicsScene(GV_graph)
        GV_graph.setScene(self.scene)
        figure = Figure()
        axes = figure.gca()
        axes.set_title("Do thi ap suat nen")
        axes.plot(self.time_points, self.pres_points, "-k", label="Ap suat ")
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
    if len(sys.argv) >= 3:
        phone_number = sys.argv[1]
        num_xilanh = int(sys.argv[2])
    else:
        raise Exception("Missing argument!")
    window = Ui(main_path=main_path,
                phone_number=phone_number,
                num_xilanh=num_xilanh)
    app.exec_()
