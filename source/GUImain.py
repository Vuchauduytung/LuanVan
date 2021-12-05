from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import numpy as np
from modules.modules_math.math_analysis import *
from modules.library.IO_support import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from math import *



class Ui(QtWidgets.QMainWindow):
    """
    Application
    """

    def __init__(self, main_path):
        super(Ui, self).__init__()
        self.main_path = main_path
        # load GUI
        gui_path = os.path.abspath(
            os.path.join(main_path, "GUI", "GUImain.ui"))
        uic.loadUi(gui_path, self)
        self.setup_widget()
        self.setup_processBar()
        self.setup_lineEdit()
        self.setup_pushButton()
        self.setup_foreseen_children()
        self.setup_tableWidget()
        self.show()

    def setup_lineEdit(self):
        LE_extTem: QLineEdit = self.findChild(QLineEdit, "LE_extTem")
        LE_comp_rat: QLineEdit = self.findChild(QLineEdit, "LE_comp_rat")
        LE_piston_jour: QLineEdit = self.findChild(QLineEdit, "LE_piston_jour")
        LE_cyl_dm: QLineEdit = self.findChild(QLineEdit, "LE_cyl_dm")
        LE_rod_len: QLineEdit = self.findChild(QLineEdit, "LE_rod_len")
        LE_xup_cor: QLineEdit = self.findChild(QLineEdit, "LE_xup_cor")
        LE_air_press: QLineEdit = self.findChild(QLineEdit, "LE_air_press")
        icon_path: str = os.path.abspath(os.path.join(
            self.main_path, "source/icon", "exclamation_mark.png"))
        icon = QIcon(icon_path)
        LE_extTem.action = LE_extTem.addAction(
            icon, LE_extTem.TrailingPosition)
        LE_comp_rat.action = LE_comp_rat.addAction(
            icon, LE_comp_rat.TrailingPosition)
        LE_piston_jour.action = LE_piston_jour.addAction(
            icon, LE_piston_jour.TrailingPosition)
        LE_cyl_dm.action = LE_cyl_dm.addAction(
            icon, LE_cyl_dm.TrailingPosition)
        LE_rod_len.action = LE_rod_len.addAction(
            icon, LE_rod_len.TrailingPosition)
        LE_xup_cor.action = LE_xup_cor.addAction(
            icon, LE_xup_cor.TrailingPosition)
        LE_air_press.action = LE_air_press.addAction(
            icon, LE_air_press.TrailingPosition)
        LE_extTem.action.setToolTip("Vui lòng nhập nhiệt độ")
        LE_comp_rat.action.setToolTip("Vui lòng nhập tỷ số nén")
        LE_cyl_dm.action.setToolTip("Vui lòng nhập hành trình piston")
        LE_piston_jour.action.setToolTip("Vui lòng nhập đường kính xi lanh")
        LE_rod_len.action.setToolTip("Vui lòng nhập chiều dài thanh truyền")
        LE_xup_cor.action.setToolTip("Vui lòng nhập góc đóng muộn Xuppap")
        LE_air_press.action.setToolTip("Vui lòng nhập áp suất khí nạp")
        LE_extTem.action.setVisible(False)
        LE_comp_rat.action.setVisible(False)
        LE_cyl_dm.action.setVisible(False)
        LE_piston_jour.action.setVisible(False)
        LE_rod_len.action.setVisible(False)
        LE_xup_cor.action.setVisible(False)
        LE_air_press.action.setVisible(False)
        LE_extTem.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_extTem,
                                                                      event=event)
        LE_comp_rat.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_comp_rat,
                                                                        event=event)
        LE_cyl_dm.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_cyl_dm,
                                                                      event=event)
        LE_piston_jour.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_piston_jour,
                                                                           event=event)
        LE_rod_len.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_rod_len,
                                                                       event=event)
        LE_xup_cor.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_xup_cor,
                                                                       event=event)
        LE_air_press.focusOutEvent = lambda event: self.LE_focusOutEvent(self=LE_air_press,
                                                                         event=event)

    def LE_focusOutEvent(UI, self: QLineEdit, event: QFocusEvent):
        if self.text() == "":
            self.action.setVisible(True)
        else:
            self.action.setVisible(False)
        QLineEdit.focusOutEvent(self, event)

    def setup_pushButton(self):
        # GB_foreseen QGroupBox
        BT_math: QPushButton = self.findChild(QPushButton, "BT_math")
        BT_clear: QPushButton = self.findChild(QPushButton, "BT_clear")
        BT_math.clicked.connect(self.BT_math_click)
        BT_clear.clicked.connect(self.BT_clear_click)
        # GB_data QGroupBox
        DSB_time: QDoubleSpinBox = self.findChild(QDoubleSpinBox, "DSB_time")
        BT_measure_xylanh1: QPushButton = self.findChild(QPushButton, "BT_measure_xylanh1")
        BT_measure_xylanh2: QPushButton = self.findChild(QPushButton, "BT_measure_xylanh2")
        BT_measure_xylanh3: QPushButton = self.findChild(QPushButton, "BT_measure_xylanh3")
        BT_measure_xylanh4: QPushButton = self.findChild(QPushButton, "BT_measure_xylanh4")
        measureBT_xilanh1_clicked = self.measureBT_click(button=BT_measure_xylanh1,
                                                        num_button=1, 
                                                        DSB_time=DSB_time)
        measureBT_xilanh2_clicked = self.measureBT_click(button=BT_measure_xylanh2,
                                                        num_button=2, 
                                                        DSB_time=DSB_time)
        measureBT_xilanh3_clicked = self.measureBT_click(button=BT_measure_xylanh3,
                                                        num_button=3, 
                                                        DSB_time=DSB_time)
        measureBT_xilanh4_clicked = self.measureBT_click(button=BT_measure_xylanh4,
                                                        num_button=4, 
                                                        DSB_time=DSB_time)
        BT_measure_xylanh1.clicked.connect(measureBT_xilanh1_clicked)
        BT_measure_xylanh2.clicked.connect(measureBT_xilanh2_clicked)
        BT_measure_xylanh3.clicked.connect(measureBT_xilanh3_clicked)
        BT_measure_xylanh4.clicked.connect(measureBT_xilanh4_clicked)
        # GB_diagnose QGroupBox
        BT_xilanh1_cancel: QPushButton = self.findChild(QPushButton, "BT_xilanh1_cancel")
        BT_xilanh2_cancel: QPushButton = self.findChild(QPushButton, "BT_xilanh2_cancel")
        BT_xilanh3_cancel: QPushButton = self.findChild(QPushButton, "BT_xilanh3_cancel")
        BT_xilanh4_cancel: QPushButton = self.findChild(QPushButton, "BT_xilanh4_cancel")
        BT_xilanh1_cancel_clicked = self.clear_xilanh_data(num_xilanh=1,
                                                           button=BT_xilanh1_cancel)
        BT_xilanh2_cancel_clicked = self.clear_xilanh_data(num_xilanh=2,
                                                           button=BT_xilanh2_cancel)
        BT_xilanh3_cancel_clicked = self.clear_xilanh_data(num_xilanh=3,
                                                           button=BT_xilanh3_cancel)
        BT_xilanh4_cancel_clicked = self.clear_xilanh_data(num_xilanh=4,
                                                           button=BT_xilanh4_cancel)
        BT_xilanh1_cancel.clicked.connect(BT_xilanh1_cancel_clicked)
        BT_xilanh2_cancel.clicked.connect(BT_xilanh2_cancel_clicked)
        BT_xilanh3_cancel.clicked.connect(BT_xilanh3_cancel_clicked)
        BT_xilanh4_cancel.clicked.connect(BT_xilanh4_cancel_clicked)
        # MainWindow
        BT_confirm: QPushButton = self.findChild(QPushButton, "BT_confirm")
        BT_cancel: QPushButton = self.findChild(QPushButton, "BT_cancel")
        # BT_cancel.clicked.connect(self.exit_gui)
        
        

    def BT_math_click(self):
        LE_extTem: QLineEdit = self.findChild(QLineEdit, "LE_extTem")
        LE_comp_rat: QLineEdit = self.findChild(QLineEdit, "LE_comp_rat")
        LE_piston_jour: QLineEdit = self.findChild(QLineEdit, "LE_piston_jour")
        LE_cyl_dm: QLineEdit = self.findChild(QLineEdit, "LE_cyl_dm")
        LE_rod_len: QLineEdit = self.findChild(QLineEdit, "LE_rod_len")
        LE_xup_cor: QLineEdit = self.findChild(QLineEdit, "LE_xup_cor")
        LE_air_press: QLineEdit = self.findChild(QLineEdit, "LE_air_press")
        math_para_lst = np.array([
            LE_extTem,
            LE_comp_rat,
            LE_piston_jour,
            LE_cyl_dm,
            LE_rod_len,
            LE_xup_cor,
            LE_air_press
        ])
        GB_foreseen: QGroupBox = self.findChild(QGroupBox, "GB_foreseen")
        if all([LE.text() != "" for LE in math_para_lst]):
            try:
                Compression_wattage, temperature_C, temperature_F, compression_pressure = caculate(extTem=float(LE_extTem.text()),
                                                                                                   comp_rat=float(LE_comp_rat.text()),
                                                                                                   piston_jour=float(LE_piston_jour.text()),
                                                                                                   cyl_dm=float(LE_cyl_dm.text()),
                                                                                                   rod_len=float(LE_rod_len.text()),
                                                                                                   xup_cor=float(LE_xup_cor.text()),
                                                                                                   air_press=float(LE_air_press.text()))
                for lineEdit in math_para_lst:
                    lineEdit.setReadOnly(True)
            except Exception:
                GB_foreseen.label_warning.setText("Vui lòng nhập chính xác tất cả thông số")
                GB_foreseen.label_warning.setVisible(True)
            else:
                GB_foreseen.label_warning.setVisible(False)
                LE_Compression: QLineEdit = self.findChild(QLineEdit, "LE_Compression")
                LE_Comp_temp_C: QLineEdit = self.findChild(QLineEdit, "LE_Comp_temp_C")
                LE_Comp_temp_F: QLineEdit = self.findChild(QLineEdit, "LE_Comp_temp_F")
                LE_watt: QLineEdit = self.findChild(QLineEdit, "LE_watt")
                LE_Compression.setText(str(round(Compression_wattage,4)))
                LE_Comp_temp_C.setText(str(round(temperature_C,4)))
                LE_Comp_temp_F.setText(str(round(temperature_F,4)))
                LE_watt.setText(str(round(compression_pressure,4)))
        else:
            GB_foreseen.label_warning.setText("Vui lòng điền đầy đủ thông tin")
            GB_foreseen.label_warning.setVisible(True)
            for LE in math_para_lst:
                if LE.text() == "":
                    LE.action.setVisible(True)
            
            
    def setup_foreseen_children(self):
        LT_input: QGridLayout = self.findChild(QGridLayout, "LT_input")
        GB_foreseen: QGroupBox = self.findChild(QGroupBox, "GB_foreseen")
        L_Warning = QLabel(GB_foreseen)
        GB_foreseen.label_warning = L_Warning
        LT_input.addWidget(L_Warning,
                           8,
                           0,
                           1,
                           2,
                           Qt.AlignCenter)
        L_Warning.setStyleSheet("QLabel { color : red; }")
        L_Warning.setVisible(False)
        
    def BT_clear_click(self):
        # GB_foreseen QGroupBox
        LE_extTem: QLineEdit = self.findChild(QLineEdit, "LE_extTem")
        LE_comp_rat: QLineEdit = self.findChild(QLineEdit, "LE_comp_rat")
        LE_piston_jour: QLineEdit = self.findChild(QLineEdit, "LE_piston_jour")
        LE_cyl_dm: QLineEdit = self.findChild(QLineEdit, "LE_cyl_dm")
        LE_rod_len: QLineEdit = self.findChild(QLineEdit, "LE_rod_len")
        LE_xup_cor: QLineEdit = self.findChild(QLineEdit, "LE_xup_cor")
        LE_air_press: QLineEdit = self.findChild(QLineEdit, "LE_air_press")
        LE_extTem.action.setVisible(False)
        LE_comp_rat.action.setVisible(False)
        LE_piston_jour.action.setVisible(False)
        LE_cyl_dm.action.setVisible(False)
        LE_rod_len.action.setVisible(False)
        LE_xup_cor.action.setVisible(False)
        LE_air_press.action.setVisible(False)
        LE_extTem.setReadOnly(False)
        LE_comp_rat.setReadOnly(False)
        LE_piston_jour.setReadOnly(False)
        LE_cyl_dm.setReadOnly(False)
        LE_rod_len.setReadOnly(False)
        LE_xup_cor.setReadOnly(False)
        LE_air_press.setReadOnly(False)
        # LE_extTem.clear()
        # LE_comp_rat.clear()
        # LE_piston_jour.clear()
        # LE_cyl_dm.clear()
        # LE_rod_len.clear()
        # LE_xup_cor.clear()
        # LE_air_press.clear()
        GB_foreseen: QGroupBox = self.findChild(QGroupBox, "GB_foreseen")
        GB_foreseen.label_warning.setVisible(False)
        # GB_data GroupBox
        LE_Compression: QLineEdit = self.findChild(QLineEdit, "LE_Compression")
        LE_Comp_temp_C: QLineEdit = self.findChild(QLineEdit, "LE_Comp_temp_C")
        LE_Comp_temp_F: QLineEdit = self.findChild(QLineEdit, "LE_Comp_temp_F")
        LE_watt: QLineEdit = self.findChild(QLineEdit, "LE_watt")
        LE_Compression.clear()
        LE_Comp_temp_C.clear()
        LE_Comp_temp_F.clear()
        LE_watt.clear()
    
    # def exit_gui(self):
        

    def setup_processBar(self):
        PB_xylanh1: QProgressBar = self.findChild(QProgressBar, "PB_xylanh1")
        PB_xylanh2: QProgressBar = self.findChild(QProgressBar, "PB_xylanh2")
        PB_xylanh3: QProgressBar = self.findChild(QProgressBar, "PB_xylanh3")
        PB_xylanh4: QProgressBar = self.findChild(QProgressBar, "PB_xylanh4")
        self.GBdata_processbar = {
            1: PB_xylanh1,
            2: PB_xylanh2,
            3: PB_xylanh3,
            4: PB_xylanh4
        }

    def setup_widget(self):
        for i in range(1,5):
            self.setup_graph_widget(num_xilanh=i)

    def setup_graph_widget(self, num_xilanh: int):
        W_graph_xilanh: QWidget = self.findChild(QWidget, "W_graph_xilanh{num}"\
            .format(num=num_xilanh))
        size = (
            W_graph_xilanh.size().width(),
            W_graph_xilanh.size().height()
        )
        chart = self.Canvas(parent=W_graph_xilanh,
                            num_xilanh=num_xilanh,
                            main_path=self.main_path,
                            size=size)
        W_graph_xilanh.chart = chart
    
    def measureBT_click(self, button: QPushButton, num_button: int, DSB_time: QDoubleSpinBox):
        xylanh_process: QProgressBar = self.GBdata_processbar[num_button]
        @asyncSlot()
        async def click(state):
            button.setEnabled(False)
            TIME = DSB_time.value()
            task = asyncio.create_task(self.run_processBar(xylanh_process=xylanh_process,
                                                           TIME=TIME))
            await task
            self.export_graph(num_xilanh=num_button,
                              TIME=TIME)
            self.activate_diagnoses_buttons(num_button=num_button)
        return click

    async def run_processBar(self, xylanh_process: QProgressBar, TIME):
        delay_time = 0.1
        step = round(TIME/delay_time)
        process_step = step/100
        check_point = 0
        for n in range(1, step+1):
            if n/process_step > check_point:
                xylanh_process.setValue(int(n/process_step))
            check_point = n/process_step
            await asyncio.sleep(0.1)
    
    # def launchPopup(self, num_xilanh: int, TIME: float):
    #     pop = self.Popup(parent=self,
    #                 num_xilanh=num_xilanh,
    #                 TIME=TIME,
    #                 main_path=self.main_path)
    #     self.pressure_val[num_xilanh] = pop.get_peak_values()
    #     self.export_table(num_xilanh=num_xilanh)
    #     pop.show()

    def export_graph(self, num_xilanh: int, TIME: float):
        TbW_diagnoses: QTabWidget = self.findChild(QTabWidget, "TbW_diagnoses")
        W_graph_xilanh: QWidget = self.findChild(QWidget, "W_graph_xilanh{num}"\
            .format(num=num_xilanh))
        chart = W_graph_xilanh.chart
        chart.draw_graph(TIME=TIME)
        self.pressure_val[num_xilanh] = chart.get_peak_values()
        self.export_table(num_xilanh=num_xilanh)
        TbW_diagnoses.setCurrentIndex(num_xilanh-1)

    def setup_tableWidget(self):
        TW_table: QTableWidget = self.findChild(QTableWidget, "TW_table")
        H_header = TW_table.horizontalHeader()
        for i in range(5):
            H_header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            # TW_table.setItem(1, i+1, QTableWidgetItem("Hello"))
        V_header = TW_table.horizontalHeader()
        for i in range(4):
            V_header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            # TW_table.setItem(i, 1, QTableWidgetItem("Hello"))
        self.pressure_val = {}

    # def setup_textEdit(self):
    #     TE_diagnoses_xilanh1: QTextEdit = self.findChild(QTextEdit, "TE_diagnoses_xilanh1")
    #     TE_diagnoses_xilanh2: QTextEdit = self.findChild(QTextEdit, "TE_diagnoses_xilanh2")
    #     TE_diagnoses_xilanh3: QTextEdit = self.findChild(QTextEdit, "TE_diagnoses_xilanh3")
    #     TE_diagnoses_xilanh4: QTextEdit = self.findChild(QTextEdit, "TE_diagnoses_xilanh4")
    #     TE_diagnoses_xilanh1.setVisible(False)
    #     TE_diagnoses_xilanh2.setVisible(False)
    #     TE_diagnoses_xilanh3.setVisible(False)
    #     TE_diagnoses_xilanh4.setVisible(False)
            
    def export_table(self, num_xilanh):
        LE_Compression: QLineEdit = self.findChild(QLineEdit, "LE_Compression")
        theory_compress_pressure = float(LE_Compression.text())
        TW_table: QTableWidget = self.findChild(QTableWidget, "TW_table")
        P_compress, P_load = self.pressure_val[num_xilanh]["compress"], self.pressure_val[num_xilanh]["load"]
        diff_ratio = abs((P_compress/theory_compress_pressure-1)*100)
        LE_air_press: QLineEdit = self.findChild(QLineEdit, "LE_air_press")
        LE_Compression: QLineEdit = self.findChild(QLineEdit, "LE_Compression")
        air_press = float(LE_air_press.text())
        compression_pressure = float(LE_Compression.text())
        state = check_state(air_press=air_press,
                            reality_pressure=self.pressure_val[num_xilanh],
                            compression_pressure=compression_pressure)
        if state:
            state_str = "Bình thường"
        else:
            state_str = "Hư hỏng"
            LE_comp_rat: QLineEdit = self.findChild(QLineEdit, "LE_comp_rat")
            LE_piston_jour: QLineEdit = self.findChild(QLineEdit, "LE_piston_jour")
            LE_cyl_dm: QLineEdit = self.findChild(QLineEdit, "LE_cyl_dm")
            LE_rod_len: QLineEdit = self.findChild(QLineEdit, "LE_rod_len")
            LE_xup_cor: QLineEdit = self.findChild(QLineEdit, "LE_xup_cor")
            LE_air_press: QLineEdit = self.findChild(QLineEdit, "LE_air_press")
            LE_air_press: QLineEdit = self.findChild(QLineEdit, "LE_air_press")
            comp_rat = float(LE_comp_rat.text())
            piston_jour = float(LE_piston_jour.text())
            cyl_dm = float(LE_cyl_dm.text())
            rod_len = float(LE_rod_len.text())
            xup_cor = float(LE_xup_cor.text())
            load_pressure = float(LE_xup_cor.text())
            pressure = self.pressure_val[num_xilanh]
            damage_str = damage(comp_rat=comp_rat,
                                piston_jour=piston_jour,
                                cyl_dm=cyl_dm,
                                rod_len=rod_len,
                                xup_cor=xup_cor,
                                air_press=air_press,
                                Pci=pressure["compress"],
                                compression_pressure=compression_pressure)
            damage_in_str = damage_in(Pmin=pressure["load"],
                                      load_pressure=load_pressure)
            assess_str = """
            <h3>Đánh gía hư hỏng:</h3>
            <p>&ensp;{damage}</p>
            <p>&ensp;{damage_in}</p>
            """\
                .format(damage=damage_str,
                        damage_in=damage_in_str)
            TE_diagnoses_xilanh: QTextEdit = self.findChild(QTextEdit, "TE_diagnoses_xilanh{num}"\
                .format(num=num_xilanh))
            TE_diagnoses_xilanh.setHtml(assess_str)
        TW_table.setItem(num_xilanh-1, 0, QTableWidgetItem(str(round(P_load, 4))))
        TW_table.setItem(num_xilanh-1, 1, QTableWidgetItem(str(round(P_compress, 4))))
        TW_table.setItem(num_xilanh-1, 2, QTableWidgetItem(LE_Compression.text()))
        TW_table.setItem(num_xilanh-1, 3, QTableWidgetItem(str(round(diff_ratio, 4))))
        TW_table.setItem(num_xilanh-1, 4, QTableWidgetItem(state_str))

    def activate_diagnoses_buttons(self, num_button: int):
        BT_xilanh_cancel: QPushButton = self.findChild(QPushButton, "BT_xilanh{num}_cancel"\
            .format(num=num_button))
        BT_xilanh_cancel.setVisible(True)
        BT_xilanh_cancel.setEnabled(True)

    def clear_table_row(self, row: int):
        TW_table: QTableWidget = self.findChild(QTableWidget, "TW_table")
        TW_table.setItem(row, 0, QTableWidgetItem(""))
        TW_table.setItem(row, 1, QTableWidgetItem(""))
        TW_table.setItem(row, 2, QTableWidgetItem(""))
        TW_table.setItem(row, 3, QTableWidgetItem(""))
        TW_table.setItem(row, 4, QTableWidgetItem(""))

    def clear_xilanh_data(self, num_xilanh: int, button: QPushButton):
        BT_measure_xylanh: QPushButton = self.findChild(QPushButton, "BT_measure_xylanh{num}"\
            .format(num=num_xilanh))
        TE_diagnoses_xilanh: QTextEdit = self.findChild(QTextEdit, "TE_diagnoses_xilanh{num}"\
            .format(num=num_xilanh))
        PB_xylanh: QProgressBar = self.findChild(QProgressBar, "PB_xylanh{num}"\
            .format(num=num_xilanh))
        W_graph_xilanh: QWidget = self.findChild(QWidget, "W_graph_xilanh{num}"\
            .format(num=num_xilanh))
        chart = W_graph_xilanh.chart
        axe = W_graph_xilanh.chart.ax
        def clear(status):
            self.clear_table_row(row=num_xilanh-1)
            BT_measure_xylanh.setEnabled(True)
            TE_diagnoses_xilanh.setHtml("")
            PB_xylanh.setValue(0)
            W_graph_xilanh.chart.ax.cla()
            axe.set(xlabel='Thời gian (s)', ylabel='Áp suất (Psi)',
                        title="Đồ thị áp suất xilanh {num}"\
                            .format(num=num_xilanh))
            axe.xaxis.set_visible(False)
            axe.yaxis.set_visible(False)
            chart.draw()
            button.setEnabled(False)
        return clear


    class Canvas(FigureCanvas):

        def __init__(self, parent, num_xilanh: int, main_path: str, size: tuple):
            self.main_path = main_path
            self.num = num_xilanh
            dpi=100
            figsize = (
                size[0]/dpi,
                size[1]/dpi
            )
            fig, self.ax = plt.subplots(figsize=figsize, 
                                        dpi=dpi)
            
            super().__init__(fig)
            self.setParent(parent)
            self.setup_data()
            """ 
            Matplotlib Script
            """
            self.period = 0.5
            self.num_point_per_period = 721
            self.ax.set(xlabel='Thời gian (s)', ylabel='Áp suất (Psi)',
                        title="Đồ thị áp suất xilanh {num}"\
                            .format(num=self.num))
            self.ax.xaxis.set_visible(False)
            self.ax.yaxis.set_visible(False)
              
            
        def draw_graph(self, TIME: float):
            epoch = int(TIME/self.period)
            t = np.linspace(start=0, 
                            stop=TIME, 
                            num=epoch*self.num_point_per_period)
            P = self.caculate_pressure(epoch=epoch)
            self.ax.plot(t, P)
            self.ax.grid()  
            self.ax.xaxis.set_visible(True)
            self.ax.yaxis.set_visible(True)
            self.ax.set(xlabel='Thời gian (s)', ylabel='Áp suất (Psi)',
                        title="Đồ thị áp suất xilanh {num}"\
                            .format(num=self.num))
            self.draw()  

        def setup_data(self):
            data_path = os.path.abspath(os.path.join(self.main_path, "source", "data"))
            engine_path = os.path.abspath(os.path.join(data_path, 'new_data.dat'))
            self.engine_data = dat2numpy(direct_path=engine_path)
    
        def caculate_pressure(self, epoch: int):
            for i in range(epoch):
                try:
                    pressure_string = np.concatenate((pressure_string, self.engine_data)) 
                except:
                    pressure_string = self.engine_data
            self.P_max = np.max(pressure_string)
            self.P_min = np.min(pressure_string)
            return pressure_string
            
        def get_peak_values(self):
            return {
                "load": self.P_min, 
                "compress": self.P_max
            }




if __name__ == "__main__":
    from asyncqt import QEventLoop, asyncSlot, asyncClose
    import asyncio
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))

    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    mainWindow = Ui(main_path=main_path)
    mainWindow.show()

    with loop:
        sys.exit(loop.run_forever())