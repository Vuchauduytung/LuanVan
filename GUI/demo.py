from PyQt5 import QtWidgets, uic
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


path = os.path.abspath(os.path.dirname(__file__))
gui_path = os.path.abspath(os.path.join(path, 'GUIinput.ui'))
                           
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(gui_path, self)
        self.setToolTip('This is QWidget')
        GB_cus_info = self.findChild(QtWidgets.QGroupBox, 'GB_customer_information')
        line_edit = GB_cus_info.findChild(QtWidgets.QLineEdit, 'LE_customer_name')
        line_edit.setObjectName("new name")
        line_edit = GB_cus_info.findChild(QtWidgets.QLineEdit, 'new name')
        # icon = app.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxCritical)
        QToolTip.setFont(QFont('SansSerif', 10))
        icon = QIcon(r'E:\AutoProject\source\icon\exclamation_mark.png')
        # add action to line edit
        action = QAction(icon, "new action", line_edit)
        line_edit.addAction(action, line_edit.TrailingPosition)
        
        action.setObjectName("action")
        action = line_edit.findChild(QtWidgets.QAction, 'action')
        # connect action.triggered signal to a slot
        action.setToolTip('Missing value')
        action.triggered.connect(lambda: print('action triggered:', line_edit.text()))
        # action.setVisible(False)
        
        # show line edit and start event loop
        graphicView = self.findChild(QtWidgets.QGraphicsView, 'GV_inciden_images')
        self.setMouseTracking(True)
        
        # pix = QPixmap(r"C:\Users\Lenovo\Pictures\Quang\6.jpg")
        # item = QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene(graphicView)
        scene_size = (graphicView.size().width()-10, graphicView.size().height()-10)
        # scene.addItem(item)
        
        Color = QColor(224,224,224)
        greenBrush = QBrush(Color)
        pen = QPen(Qt.blue)
        pen.setStyle(Qt.PenStyle.DashLine)
        pen.setWidth(2)
        rect = scene.addRect(0, 0, scene_size[0], scene_size[1], pen, greenBrush)
        
        x_center = graphicView.size().width()/2
        y_center = graphicView.size().height()/2
        
        # passive_text_1 = scene.addText("Drag image here.")
        # passive_text_2 = scene.addText("Or")
        # active_text = scene.addText("choose file")
        passive_text_1 = QGraphicsTextItem("Drag image here.")
        passive_text_2 = QGraphicsTextItem("Or")
        active_text = QGraphicsTextItem("choose file")
        scene.addItem(passive_text_1)
        scene.addItem(passive_text_2)
        scene.addItem(active_text)
        
        passive_text_1_font = QFont("Times", 14, QFont.Bold)
        passive_text_2_font = QFont("Times", 10)
        active_text_font = QFont("Times", 10)
        active_text.setDefaultTextColor(Qt.blue)
        # active_text_font.setDefaultTextColor()
        
        passive_text_1.setFont(passive_text_1_font)
        passive_text_2.setFont(passive_text_2_font)
        active_text.setFont(active_text_font)
             
        passive_text_1_pos = (
            x_center - passive_text_1.boundingRect().width()/2,
            y_center - (passive_text_1.boundingRect().height()+passive_text_2.boundingRect().height())/2
        )
        
        passive_text_2_pos = (
            x_center - (passive_text_2.boundingRect().width()+active_text.boundingRect().width())/2,
            passive_text_1_pos[1] + passive_text_1.boundingRect().height()
        )
        
        active_text_pos = (
            passive_text_2_pos[0] + passive_text_2.boundingRect().width(),
            passive_text_2_pos[1]
        )
        
        passive_text_1.setPos(passive_text_1_pos[0], passive_text_1_pos[1])
        passive_text_2.setPos(passive_text_2_pos[0], passive_text_2_pos[1])
        active_text.setPos(active_text_pos[0], active_text_pos[1])
        
        active_text.setAcceptedMouseButtons(Qt.AllButtons)
        active_text.setAcceptTouchEvents(True)
        # scene.mousePressEvent = mousePressEvent
        active_text.mousePressEvent = mousePressEvent
        
        graphicView.setScene(scene)
        
        label_warning = self.findChild(QtWidgets.QLabel, 'label_warning')
        label_warning.hide()
        
        button = self.findChild(QtWidgets.QPushButton, 'BT_confirm')
        button.setIcon(icon)
        
        checkbox = self.findChild(QtWidgets.QCheckBox, 'CB_incident_1')
        checkbox.setIcon(icon)
        
        self.show()
        

def mousePressEvent(event):
        if event.button() == Qt.LeftButton:
            print("Press mouse")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()