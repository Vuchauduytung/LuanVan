from PyQt5 import QtWidgets, uic, QtGui
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

    def __init__(self, main_path: str, phone_number: str):
        super(Ui, self).__init__()
        self.main_path = main_path
        self.phone_number = phone_number
        # load GUI
        gui_path = os.path.abspath(
            os.path.join(main_path, "GUI", "GUIgraph_fix.ui"))
        uic.loadUi(gui_path, self)
        self.setup_pushButton()
        self.setup_graph()
        self.icon()
        self.show()
    
    def icon(self):
        self.setWindowIcon(QIcon('source\icon\Logo BK.png'))
        
    def setup_pushButton(self):
        # GB_informatin_custom QGroupBox
        BT_exit: QPushButton = self.findChild(QPushButton, "BT_exit")
        BT_exit.clicked.connect(self.BT_quit_click)
    
    def setup_graph(self):
        #Luu gia tri vao file json
        GV_graph_fix: QGraphicsView = self.findChild(QGraphicsView, "GV_graph_fix")
        data_path = os.path.abspath(os.path.join(self.main_path, "data", "customers_data.json"))
        customers_list = json2dict(data_path)
        for customer in customers_list:
            if customer.get('phone_number') == self.phone_number:
                break
        else:
            raise Exception("Cannot find customer with phone number \"{phone_number}\""\
                .format(phone_number=self.phone_number))
        # Lay gia tri grap trong json
        images_code_list = customer["images"]
        self.scene = QtWidgets.QGraphicsScene(self.GV_graph_fix)
        self.GV_graph_fix.setScene(self.scene)
        # Position image
        pos = [0,0]
        pos_2 = [0,0]
        # Pixel image
        pixel = [750,450]
        # Count number of values in list Filename 
        k = 0
        # Count value in list grap
        i = 0
        for img_code in images_code_list:
            image_qt = decode_img(code=img_code)
            i += 1
            k = float(len(images_code_list))
            if k <2:
                image_qt = image_qt.scaled(int(pixel[0]), int(pixel[1]))
                Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(image_qt))
                self.scene.addItem(Pimax_Item) 
                self.GV_graph_fix.fitInView(Pimax_Item)
            elif k>=2:
                if i <= round(k/2):        
                    image_qt = image_qt.scaled(int(pixel[0]/round(k/2)), int(pixel[1]/2))
                    Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(image_qt))
                    self.scene.addItem(Pimax_Item)
                    Pimax_Item.setOffset(int(pos[0]), int(pos[1])) 
                    pos[0] += (pixel[0]+5)/round(k/2) 
                elif i > round(k/2):
                    pos_2[1] = (pixel[1]+5)/2
                    image_qt = image_qt.scaled(int(pixel[0]/(k-round(k/2))), int(pixel[1]/2))
                    Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(image_qt))
                    self.scene.addItem(Pimax_Item)
                    Pimax_Item.setOffset(int(pos_2[0]), int(pos_2[1]))
                    pos_2[0] += (pixel[0]+5)/(k-round(k/2))
        
    def BT_quit_click(self):
        window.close()
        
    

if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    if len(sys.argv) > 1:
        phone_number = sys.argv[1]
    else:
        raise Exception("Missing phone number")
    window = Ui(main_path=main_path,
                phone_number=phone_number)
    app.exec_()
