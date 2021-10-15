from PyQt5 import QtWidgets, uic
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


path = os.path.abspath(os.path.dirname(__file__))
gui_path = os.path.abspath(os.path.join(path, 'GUIinput.ui'))
modules_path = os.path.abspath(os.path.join(path, os.pardir, "source", 'modules'))      
sys.path.append(modules_path)

from library.format_translate import *                    
                           
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(gui_path, self)
        self.setToolTip('This is QWidget')
        GB_cus_info = self.findChild(QtWidgets.QGroupBox, 'GB_customer_information')

        font = QFont("Arial", 
                     0,
                     99,
                     False)
        GB_cus_info.setFont(font)
        line_edit = GB_cus_info.findChild(QtWidgets.QLineEdit, 'LE_customer_name')
        line_edit.setObjectName("new name")
        line_edit = GB_cus_info.findChild(QtWidgets.QLineEdit, 'new name')
        
        font = QFont("Arial", 
                     0,
                     99,
                     True)
        
        line_edit.setFont(font)

        
        # icon = app.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxCritical)
        QToolTip.setFont(QFont('SansSerif', 10))
        icon = QIcon(r'E:\AutoProject\source\icon\exclamation_mark.png')
        # add action to line edit
        action = QAction("new action", line_edit)
        action.setIcon(icon)
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
        scene_size = (graphicView.size().width(), graphicView.size().height())
        # scene.addItem(item)
        
        Color = QColor(224,224,224)
        greenBrush = QBrush(Color)
        pen = QPen(Qt.blue)
        pen.setStyle(Qt.PenStyle.DashLine)
        pen.setWidth(2)
        rect = scene.addRect(0, 0, scene_size[0], scene_size[1], pen, greenBrush)
        rect.setScale(0.98)
                
        x_center = graphicView.size().width()/2
        y_center = graphicView.size().height()/2
        
        # passive_text_1 = scene.addText("Drag image here.")
        # passive_text_2 = scene.addText("Or")
        # active_text = scene.addText("choose file")
        passive_text_1 = QGraphicsTextItem("Drag image here.")
        passive_text_2 = QGraphicsTextItem("Or")
        active_text = QGraphicsTextItem("choose file")
        # scene.addItem(passive_text_1)
        # scene.addItem(passive_text_2)
        # scene.addItem(active_text)
        
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
        scene.mousePressEvent = mousePressEvent_lambda(self)
        # active_text.mousePressEvent = mousePressEvent
        
        graphicView.setScene(scene)
        
        label_warning = self.findChild(QtWidgets.QLabel, 'Label_customer_information_warning')
        # label_warning.hide()
        label_warning.setTextFormat(Qt.RichText)
        label_warning.setText("<b>This text is bold</b>")
        pixmap = icon.pixmap(QSize(20,20), QIcon.Selected)
        label_warning.setPixmap(pixmap)
        
        button = self.findChild(QtWidgets.QPushButton, 'BT_confirm')
        button.setIcon(icon)
        button.setFont(font)

        
        checkbox = self.findChild(QtWidgets.QCheckBox, 'CB_incident_1')
        checkbox.setIcon(icon)

        
        TextItem = QGraphicsTextItem()
        self.document_ = TextItem.document()
        rootframe = TextItem.document().rootFrame()
        cursor = rootframe.firstCursorPosition()
        cursor.insertHtml(
            '''
                <!DOCTYPE html>
                <html>
                <head>
                <style>

                .center {
                    margin: 0;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    -ms-transform: translate(-50%, -50%);
                    transform: translate(-50%, -50%);
                }
                </style>
                </head>
                <body>


                <div class="center">
                <p>I am vertically and horizontally centered.</p>
                </div>


                </body>
                </html>
            '''
        )
        # curs_max=cursor.position()
        # self.my_callback = QGraphicsTextItem_callback(curs_min=curs_min, 
        #                                               curs_max=curs_max)
        scene.addItem(TextItem)
        
        l = QAction(GB_cus_info)
        # l.setAccessibleName("Hello")
        TextItem.document().setPageSize(QSizeF( 1000,1000))
        # self.p = QPointF()
        
        self.show()
        

def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
        print("Press mouse")
        pos = event.scenePos()
        self.p = QPointF(pos.x(), pos.y())
        print(self.p.x())
        print(self.p.y())
        documentLayout = self.document_.documentLayout()
        cur_pos = documentLayout.hitTest(self.p, 
                                         Qt.ExactHit)
        if cur_pos > self.my_callback.curs_min and cur_pos < self.my_callback.curs_max:
            print("chose file callback")
        print(cur_pos)
        
        
def mousePressEvent_lambda(self):
    return lambda event: mousePressEvent(self, event)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

