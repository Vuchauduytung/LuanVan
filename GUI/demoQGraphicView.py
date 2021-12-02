from PyQt5 import QtWidgets, uic
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

def main():

    app = QApplication(sys.argv)

    grview = QGraphicsView()
    scene = QGraphicsScene(grview)
    scene.setSceneRect(0, 0, 680, 459)
    grview.setScene(scene)
    for _ in range(10):
        item = GraphicsRectItem(0, 0, 300, 150)
        scene.addItem(item)
        item.setPos(QPointF(*random.sample(range(300), 2)))

    grview.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
    grview.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()