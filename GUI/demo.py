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

from library.pyqt_support import *                    
                           
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
        action.setIconText("Hello")
        
        action.setObjectName("action")
        action = line_edit.findChild(QtWidgets.QAction, 'action')
        # connect action.triggered signal to a slot
        action.setToolTip('Missing value')
        action.triggered.connect(lambda: print('action triggered:', line_edit.text()))
        # action.setVisible(False)
        
        
        # show line edit and start event loop
        graphicView = self.findChild(QtWidgets.QGraphicsView, 'GV_inciden_images')
        # self.setMouseTracking(True)
        
        # pix = QPixmap(r"C:\Users\Lenovo\Pictures\Quang\6.jpg")
        # item = QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene(graphicView)
        scene_size = (graphicView.size().width(), graphicView.size().height())
        # scene.addItem(item)
        # graphicView.setSceneRect(0, 0, scene_size[0], scene_size[1])
        Color = QColor(224,224,224)
        greenBrush = QBrush()
        greenBrush.setColor(Color)
        color1 = QColor(50, 80, 168)
        pen = QPen(color1)
        pen.setStyle(Qt.PenStyle.DashLine)
        pen.setWidth(2)
        rect = QGraphicsRectItem(0, 0, scene_size[0], scene_size[1])
        rect.setPen(pen)
        rect.setBrush(greenBrush)
        scene.addItem(rect)
        rect.setScale(0.98)
        # graphicView.fitInView(scene.sceneRect())
                
        x_center = graphicView.size().width()/2
        y_center = graphicView.size().height()/2
        
        scene.mouseMoveEvent = mousePressEvent_lambda(self)
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
        self.document_.setHtml(
            '''
                <STYLE type="text/css">
                DIV.mypars {
                    text-align: center; 
                }
                </STYLE>
                <BODY>
                <DIV class="mypars">
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <P style="color:red">Drag image here </P>
                <P>Or <b>choose file</b> </P>
                </DIV>
            '''
        )
        curs_max=cursor.position()
        self.my_callback = QGraphicsTextItem_callback(curs_min=33, 
                                                      curs_max=curs_max)
        scene.addItem(TextItem)
        TextItem.installEventFilter(self)
        l = QAction(GB_cus_info)
        # l.setAccessibleName("Hello")
        # TextItem.document().setPageSize(QSizeF(scene_size[0]*0.9, scene_size[1]*0.9))
        # TextItem.update(0, 0, 1, 1)
        self.p = QPointF()
        
        DE_fixing_date = self.findChild(QtWidgets.QDateEdit, 'DE_fixing_date')
        DE_fixing_date.setAccessibleName("Hello")
        DE_fixing_date.addAction(action)
        # date = QDate(2020, 6, 10)
        date = QDate.fromString(None, "yyyy-MM-dd")
        DE_fixing_date.setDate(date)
        self.show()
        
    # def eventFilter(self, object, event):
    #     if event.type() == QEvent.GraphicsSceneHoverMove:
    #         print("Mouse is over the label")
    #         self.stop = True
    #         print('program stop is', self.stop)
    #         return True
    #     elif event.type() == QEvent.GraphicsSceneHoverLeave:
    #         print("Mouse is not over the label")
    #         self.stop = False
    #         print('program stop is', self.stop)
    #     return False    
        

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
    else: 
        print("Mouse move event")

# def eventFilter(self, object, event):
#     if event.type() == QEvent.Enter:
#         print("Mouse is over the label")
#         self.stop = True
#         print('program stop is', self.stop)
#         return True
#     elif event.type() == QEvent.Leave:
#         print("Mouse is not over the label")
#         self.stop = False
#         print('program stop is', self.stop)
#         return False
        
        
def mousePressEvent_lambda(self):
    return lambda event: mousePressEvent(self, event)

# def eventFilter_lambda(self):
#     return lambda event, object: eventFilter(self, object, event)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

