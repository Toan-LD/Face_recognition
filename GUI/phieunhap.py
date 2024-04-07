# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/phieunhap.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from DAO.ctpnDAO import ctpnDAO
from DAO.phieunhapDAO import phieunhapDAO
from DAO.employeeDAO import employeeDAO
from DAO.supplierDAO import supplierDAO
from DAO.medicineDAO import medicineDAO
from DTO.phieunhapDTO import PhieuNhap
from DTO.ctpnDTO import CTPN
from GUI.phieunhap_dialog import Ui_phieunhap_dialog
from GUI.ctpn_dialog import Ui_ctpn_dialog
import GUI.mesage_box as msg

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(875, 561)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(7)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.txtSearchPN = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtSearchPN.setMinimumSize(QtCore.QSize(0, 32))
        self.txtSearchPN.setObjectName("txtSearchPN")
        self.horizontalLayout_5.addWidget(self.txtSearchPN)
        self.btnSearchPN = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSearchPN.setMinimumSize(QtCore.QSize(40, 40))
        self.btnSearchPN.setStyleSheet("background-color: #BDD5D7;\n"
"border-radius: 5px;\n"
"border: none;")
        self.btnSearchPN.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearchPN.setIcon(icon)
        self.btnSearchPN.setObjectName("btnSearchPN")
        self.horizontalLayout_5.addWidget(self.btnSearchPN)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.table_phieunhap = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_phieunhap.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_phieunhap.setObjectName("table_phieunhap")
        self.table_phieunhap.setColumnCount(5)
        self.table_phieunhap.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_phieunhap.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_phieunhap.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_phieunhap.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_phieunhap.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_phieunhap.setHorizontalHeaderItem(4, item)
        self.table_phieunhap.horizontalHeader().setStretchLastSection(True)
        self.table_phieunhap.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.table_phieunhap)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.btnAddCTNP = QtWidgets.QPushButton(self.groupBox)
        self.btnAddCTNP.setMinimumSize(QtCore.QSize(40, 40))
        self.btnAddCTNP.setStyleSheet("background-color: #9FC899;\n"
"border-radius: 5px;\n"
"border: none;")
        self.btnAddCTNP.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddCTNP.setIcon(icon1)
        self.btnAddCTNP.setObjectName("btnAddCTNP")
        self.horizontalLayout_6.addWidget(self.btnAddCTNP)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.table_ctpn = QtWidgets.QTableWidget(self.groupBox)
        self.table_ctpn.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_ctpn.setObjectName("table_ctpn")
        self.table_ctpn.setColumnCount(5)
        self.table_ctpn.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_ctpn.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ctpn.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ctpn.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ctpn.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ctpn.setHorizontalHeaderItem(4, item)
        self.table_ctpn.horizontalHeader().setStretchLastSection(True)
        self.table_ctpn.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.table_ctpn)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget.setStyleSheet("QWidget{\n"
"    background-color: #BDD5D7;\n"
"    border:1px solid black\n"
"}\n"
"QLabel{\n"
"    border:none\n"
"}\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setContentsMargins(11, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(8, 5, 8, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnAdd = QtWidgets.QPushButton(self.widget_3)
        self.btnAdd.setMinimumSize(QtCore.QSize(90, 40))
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setStyleSheet("background-color: #9FC899;\n"
"border: none;\n"
"border-radius: 5px;")
        self.btnAdd.setIcon(icon1)
        self.btnAdd.setIconSize(QtCore.QSize(20, 20))
        self.btnAdd.setFlat(False)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 40))
        self.pushButton.setStyleSheet("background-color: #BDD5D7;\n"
"border-radius: 5px;\n"
"border: none;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_3, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "THÔNG TIN PHIẾU NHẬP"))
        item = self.table_phieunhap.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã phiếu nhập"))
        item = self.table_phieunhap.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Mã nhân viên"))
        item = self.table_phieunhap.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mã nhà cung cấp"))
        item = self.table_phieunhap.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Ngày lập"))
        item = self.table_phieunhap.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tổng tiền"))
        self.groupBox.setTitle(_translate("Form", "CHI TIẾT PHIẾU NHẬP"))
        item = self.table_ctpn.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã phiếu nhập"))
        item = self.table_ctpn.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Mã dược phẩm"))
        item = self.table_ctpn.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Số lượng"))
        item = self.table_ctpn.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Đơn giá"))
        item = self.table_ctpn.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Thành tiền"))
        self.label.setText(_translate("Form", "Quản lý phiếu nhập"))
        self.btnAdd.setText(_translate("Form", "Thêm"))
        self.pushButton.setText(_translate("Form", "Reset"))
        self.loadPhieuNhapData()
        self.table_phieunhap.itemClicked.connect(self.on_table_phieunhap_clicked)
        self.btnAdd.clicked.connect(self.show_add_pn_dialog)
        self.btnAddCTNP.clicked.connect(self.show_add_ctpn_dialog)

    def fillTablePhieuNhap(self, pn_list):
        row = 0
        self.table_phieunhap.setRowCount(len(pn_list))
        for pn in pn_list:
            self.table_phieunhap.setItem(row, 0, QtWidgets.QTableWidgetItem(str(pn.getMaPN())))
            self.table_phieunhap.setItem(row, 1, QtWidgets.QTableWidgetItem(str(pn.getMaNV())))
            self.table_phieunhap.setItem(row, 2, QtWidgets.QTableWidgetItem(str(pn.getMaNCC())))
            self.table_phieunhap.setItem(row, 3, QtWidgets.QTableWidgetItem(str(pn.getNgayTao())))
            self.table_phieunhap.setItem(row, 4, QtWidgets.QTableWidgetItem(str(pn.getTongTien())))
            row = row +1

    def fillTableCTPN(self, ctpn_list):
        row = 0
        self.table_ctpn.setRowCount(len(ctpn_list))
        for ctpn in ctpn_list:
            self.table_ctpn.setItem(row, 0, QtWidgets.QTableWidgetItem(str(ctpn.getMaPN())))
            self.table_ctpn.setItem(row, 1, QtWidgets.QTableWidgetItem(str(ctpn.getMaDP())))
            self.table_ctpn.setItem(row, 2, QtWidgets.QTableWidgetItem(str(ctpn.getSoLuong())))
            self.table_ctpn.setItem(row, 3, QtWidgets.QTableWidgetItem(str(ctpn.getGia())))
            self.table_ctpn.setItem(row, 4, QtWidgets.QTableWidgetItem(str(ctpn.getThanhTien())))
            row = row +1

    def loadPhieuNhapData(self):
        dao = phieunhapDAO()
        pn_list = dao.getAllPhieuNhap()
        self.fillTablePhieuNhap(pn_list)

    def on_table_phieunhap_clicked(self):
        selected_items = self.table_phieunhap.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            id = self.table_phieunhap.item(selected_row, 0).text()
            dao = ctpnDAO()
            ctpn_list = dao.getCTPNById(id)
            self.fillTableCTPN(ctpn_list)

    def show_add_pn_dialog(self):
        dialog = QtWidgets.QDialog()
        self.phieunhap_dialog = Ui_phieunhap_dialog()
        self.phieunhap_dialog.setupUi(dialog)
        self.loadComboboxMaNV()
        self.loadComboboxMaNCC()
        self.phieunhap_dialog.btnAccept.clicked.connect(self.addPhieuNhap)
        dialog.exec_()
        dialog.show()

    def show_add_ctpn_dialog(self):
        dialog = QtWidgets.QDialog()
        self.ctpn_dialog = Ui_ctpn_dialog()
        self.ctpn_dialog.setupUi(dialog)
        self.loadComboboxMaDP()

        selected_items = self.table_phieunhap.selectedItems()
        if not selected_items:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng dược phẩm")
            return
        
        selected_row = selected_items[0].row()
        id = self.table_phieunhap.item(selected_row, 0).text()
        
        self.ctpn_dialog.cbMaDP.currentIndexChanged.connect(self.loadPriceOfMedicine)
        self.ctpn_dialog.btnAccept.clicked.connect(lambda: self.addCTPN(id))
        dialog.exec_()
        dialog.show()

    def loadPriceOfMedicine(self):
        madp = self.ctpn_dialog.cbMaDP.currentText().split("-")[0]
        dao = medicineDAO()
        medicine = dao.getMedicineById(madp)
        self.ctpn_dialog.txtPrice.setText(str(medicine.getGia()))

    def loadComboboxMaNV(self):
        dao = employeeDAO()
        employees = dao.find_All()

        for emp in employees:
            self.phieunhap_dialog.cbMaNV.addItem(f"{emp.manv} - {emp.tennv}")

    def loadComboboxMaNCC(self):
        dao = supplierDAO()
        suppliers = dao.getAllSuppliers()

        for supplier in suppliers:
            self.phieunhap_dialog.cbMaNCC.addItem(f"{supplier.getMaNCC()} - {supplier.getTenNCC()}")

    def loadComboboxMaDP(self):
        dao = medicineDAO()
        medicines = dao.getAllMedicines()

        for m in medicines:
            self.ctpn_dialog.cbMaDP.addItem(f"{m.getMaDP()} - {m.getTenDP()}")


    def addPhieuNhap(self):
        manv = self.phieunhap_dialog.cbMaNV.currentText().split("-")[0]
        mancc = self.phieunhap_dialog.cbMaNCC.currentText().split("-")[0]
        ngaytao = self.phieunhap_dialog.dateNgayTao.date().toString('MM-dd-yyyy')

        dao = phieunhapDAO()
        dao.insertPhieuNhap(PhieuNhap(None, manv, mancc, ngaytao, 0))
        msg.show_info_messagebox("Thêm phiếu nhập thành công")
        self.loadPhieuNhapData()

    def addCTPN(self, mapn):
        madp = self.ctpn_dialog.cbMaDP.currentText().split("-")[0]
        gia = self.ctpn_dialog.txtPrice.text()
        sl = self.ctpn_dialog.txtQty.text()
        thanhtien = int(gia) * int(sl)

        if not sl:
            msg.show_warning_messagebox("Vui lòng nhập đầy đủ dữ liệu")
            return
    
        dao = ctpnDAO()
        dao.insertCTPN(CTPN(mapn, madp, sl, gia, thanhtien))
        msg.show_info_messagebox("Thêm phiếu nhập thành công")
        self.on_table_phieunhap_clicked()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
