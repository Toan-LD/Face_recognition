from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets 

from GUI.sidebar import Ui_MainWindow
from GUI.add_service_dialog import Ui_add_service_dialog
import GUI.nhanvien as nv
import GUI.dichvu as dv
import GUI.phieunhap as pn
import GUI.duocpham as dp

class Main_Page(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.window = QMainWindow()
        self.setupUi(self)
        self.show()

        self.icon_menu_widget.hide()

        self.nv_form = nv.Ui_Form()
        self.nv_form.setupUi(self.employee_page)

        self.dv_form = dv.Ui_Form()
        self.dv_form.setupUi(self.service_Page)

        self.pn_form = pn.Ui_Form()
        self.pn_form.setupUi(self.phieunhap_page)

        self.dp_form = dp.Ui_Form()
        self.dp_form.setupUi(self.medicine_page)

        self.eventHandling()
        self.dv_form.btnAdd.clicked.connect(self.show_add_dialog)
        self.connection = get_sql_connection()
        self.loadServiceData()

    def showHome_Pages(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def showCustomer_Pages(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def showPets_Pages(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def showEmployee_Pages(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def showPhieuNhap_Pages(self):
        self.stackedWidget.setCurrentIndex(4)

    def showMedicine_Pages(self):
        self.stackedWidget.setCurrentIndex(5)

    def showService_Pages(self):
        self.stackedWidget.setCurrentIndex(6)

    def showChart_Pages(self):
        self.stackedWidget.setCurrentIndex(7)
    
    def show_add_dialog(self):
        dialog = QtWidgets.QDialog()
        add_dialog_ui = Ui_add_service_dialog()
        add_dialog_ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def loadServiceData(self):
        services = getAllServices(self.connection)
        row = 0
        self.dv_form.table_service.setRowCount(len(services))
        for service in services:
            self.dv_form.table_service.setItem(row, 0, QtWidgets.QTableWidgetItem(str(service.getMaDV())))
            self.dv_form.table_service.setItem(row, 1, QtWidgets.QTableWidgetItem(service.getTen()))
            self.dv_form.table_service.setItem(row, 2, QtWidgets.QTableWidgetItem(str(service.getGia())))
            self.dv_form.table_service.setItem(row, 3, QtWidgets.QTableWidgetItem(str(service.getMaLoaiDV())))
            row = row +1

    # Xử lý giao diện
    def eventHandling(self):
        self.btnEmployee.clicked.connect(self.showEmployee_Pages)
        self.btnCustomer.clicked.connect(self.showCustomer_Pages)
        self.btnPets.clicked.connect(self.showPets_Pages)
        self.btnChart.clicked.connect(self.showChart_Pages)
        self.btnHome.clicked.connect(self.showHome_Pages)
        self.btnService.clicked.connect(self.showService_Pages)
        self.btnPhieuNhap.clicked.connect(self.showPhieuNhap_Pages)
        self.btnMedicine.clicked.connect(self.showMedicine_Pages)
        self.iconEmployee.clicked.connect(self.showEmployee_Pages)
        self.iconCustomer.clicked.connect(self.showCustomer_Pages)
        self.iconPets.clicked.connect(self.showPets_Pages)
        self.iconChart.clicked.connect(self.showChart_Pages)
        self.iconHome.clicked.connect(self.showHome_Pages)
        self.iconService.clicked.connect(self.showService_Pages)
        self.iconPhieuNhap.clicked.connect(self.showPhieuNhap_Pages)
        self.iconMedicine.clicked.connect(self.showMedicine_Pages)


