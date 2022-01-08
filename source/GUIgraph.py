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
        self.setup_action()
        self.show()

    def setup_action(self):
        actionSave: QAction = self.findChild(QAction, "actionSave")
        actionSave.triggered.connect(self.save_image)

    def save_image(self):
        filepath = self.get_saveFile_directory()
        # Get region of scene to capture from somewhere.
        area = self.scene.sceneRect()
        # Create a QImage to render to and fix up a QPainter for it.
        image = QImage(int(area.width()), int(area.height()), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(image)
        # Render the region of interest to the QImage.
        self.scene.render(painter, area, area)
        painter.end()
        # Save the image to a file.
        image.save(filepath)
        

    def get_saveFile_directory(self):
        default_dir = os.path.abspath(os.path.join(self.main_path, "output"))
        default_filename = os.path.join(default_dir, "graph.png")
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save audio file", default_filename, "Excel Files (*.png)"
        )
        if filename:
            print(filename)
        return filename    

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
        icon_path = os.path.abspath(os.path.join(self.main_path, "icon","Logo BK.png"))
        self.setWindowIcon(QIcon(icon_path))
    # Hien do thi giong GUI main
    def setup_graph(self):
        GV_graph: QGraphicsView = self.findChild(QGraphicsView, "GV_graph")
        # Ve do thi ap suat nen   
        self.scene = QtWidgets.QGraphicsScene(GV_graph)
        GV_graph.setScene(self.scene)
        figure: Figure = Figure()
        axes = figure.gca()
        axes.set_title("Đồ thị áp suất xi lanh {num_xilanh}"\
            .format(num_xilanh=self.num_xilanh))
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
    main_path = os.path.abspath(os.path.dirname(__file__))
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
