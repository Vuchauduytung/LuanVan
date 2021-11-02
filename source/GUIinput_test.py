from PyQt5 import QtWidgets, uic
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from modules.library.IO_support import *
from modules.library.pyqt_support import *
from modules.library.pyqt_event import *
from modules.library.pyqt_extension_method import *


class Ui(QtWidgets.QMainWindow):
    """
    Application
    """

    def __init__(self, main_path, driver):
        super(Ui, self).__init__()
        gui_loc = driver.get("path")
        gui_path = os.path.abspath(os.path.join(main_path, gui_loc))
        self.main_path = main_path

        # load GUI
        uic.loadUi(gui_path, self)

        # GUI config here
        # --------------------------
        self.GUI_init(driver=driver)

        # --------------------------

        # Show GUI and start event loop
        self.show()

    def GUI_init(self, driver: dict):
        """Khởi tạo tất cả các thuộc tính cũng như các Object
        con của GUI        

        Args:
            driver (dict): driver cho việc thiết lập GUI
        """
        GUI_name = self.objectName()
        assert GUI_name == driver.get("name"), "GUI name does not match"

        self.desc = driver.get("desc")
        self.setWindowTitle(driver.get("text"))

        dim = driver.get("dimension")
        if dim is not None:
            self.resize(dim.get("width"), dim.get("height"))

        icon_prop = driver.get("icon")
        icon_path = icon_prop.get("path")
        if icon_path is not None:
            pixmap = QPixmap(os.path.abspath(os.path.join(self.main_path, icon_path)))
            icon_size = icon_prop.get("size")
            if icon_size is not None:
                icon = QIcon(pixmap.scaled(icon_size[0], icon_size[1]))
            else:
                icon = QIcon(pixmap)
            self.setWindowIcon(icon)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.childConfig = childConfig_lambda(self)
        self.childConfig(child_prop=driver.get("children"),
                         GUI=self,
                         main_path=self.main_path)
        self.setMouseTracking(True)
        self.p = QPointF()

    def eventFilter(self, obj, event):
        """Bắt event của Application

        Args:
            obj (Any): object nhận được event
            event (QEvent): event bắt được

        Returns:
            bool: 
                True, nếu muốn dừng nhận các event kế tiếp \n
                False, nếu muốn tiếp tục bắt event
        """
        return MouseEvent.run(obj=obj,
                              event=event,
                              point=self.p)


def main():
    driver_path = r"F:\HK211\Luận Văn\source\drivers\GUIinput.json"
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    driver = json2dict(direct_path=driver_path)

    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path,
                driver=driver)
    app.exec_()


if __name__ == "__main__":
    main()
