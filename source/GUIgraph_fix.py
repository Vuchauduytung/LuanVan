from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from modules.library.IO_support import *
from modules.library.pyqt_support import *


class Ui(QtWidgets.QMainWindow):
    """
    Application
    """

    def __init__(self, main_path):
        super(Ui, self).__init__()
        self.main_path = main_path
        # load GUI
        gui_path = os.path.abspath(
            os.path.join(main_path, "GUI", "GUIgraph_fix.ui"))
        uic.loadUi(gui_path, self)
        self.setup_pushButton()
        self.setup_graph()
        self.show()
        
    def setup_pushButton(self):
        # GB_informatin_custom QGroupBox
        BT_exit: QPushButton = self.findChild(QPushButton, "BT_exit")
        BT_exit.clicked.connect(self.BT_quit_click)
    
    def setup_graph(self):
        #Luu gia tri vao file json
        GV_graph_fix: QGraphicsView = self.findChild(QGraphicsView, "GV_graph_fix")
        data_path = os.path.abspath(os.path.join(self.main_path, "source", "data.json"))
        customer = json2dict(data_path)
        # Lay gia tri grap trong json
        grap = customer["grap"]
        self.scene = QtWidgets.QGraphicsScene(self.GV_graph_fix)
        self.GV_graph_fix.setScene(self.scene)
        # Position imge
        pos = [0,0]
        pos_2 = [0,0]
        # Pixel image
        pixel = [750,450]
        # Count number of values in list Filename 
        k = 0
        # Count value in list grap
        i = 0
        for grap[i] in grap:
            img = QtGui.QImage(grap[i])
            i += 1
            k = float(len(grap))
            if k <2:
                img = img.scaled(pixel[0], pixel[1])
                Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
                a = self.scene.addItem(Pimax_Item) 
                self.GV_graph_fix.fitInView(Pimax_Item)
            elif k>=2:
                if i <= round(k/2):        
                    img = img.scaled(pixel[0]/round(k/2), pixel[1]/2)
                    Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
                    a = self.scene.addItem(Pimax_Item)
                    Pimax_Item.setOffset(pos[0], pos[1]) 
                    pos[0] += (pixel[0]+5)/round(k/2) 
                elif i > round(k/2):
                    pos_2[1] = (pixel[1]+5)/2
                    img = img.scaled(pixel[0]/(k-round(k/2)),pixel[1]/2)
                    Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
                    a = self.scene.addItem(Pimax_Item)
                    Pimax_Item.setOffset(pos_2[0], pos_2[1])
                    pos_2[0] += (pixel[0]+5)/(k-round(k/2))
        
    def BT_quit_click(self):
        window.close()
        
    

if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path)
    app.exec_()
