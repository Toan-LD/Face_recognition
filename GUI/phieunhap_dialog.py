# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/phieunhap_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_phieunhap_dialog(object):
    def setupUi(self, phieunhap_dialog):
        phieunhap_dialog.setObjectName("phieunhap_dialog")
        phieunhap_dialog.resize(400, 322)
        phieunhap_dialog.setMinimumSize(QtCore.QSize(400, 276))
        self.label = QtWidgets.QLabel(phieunhap_dialog)
        self.label.setGeometry(QtCore.QRect(50, 90, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(phieunhap_dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 111, 16))
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(phieunhap_dialog)
        self.widget.setGeometry(QtCore.QRect(0, -1, 401, 61))
        self.widget.setStyleSheet("background-color: rgb(0, 255, 244);\n"
"border:1px solid black;")
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:none;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.txtTotalPrice = QtWidgets.QLineEdit(phieunhap_dialog)
        self.txtTotalPrice.setGeometry(QtCore.QRect(170, 210, 181, 21))
        self.txtTotalPrice.setObjectName("txtTotalPrice")
        self.btnAccept = QtWidgets.QPushButton(phieunhap_dialog)
        self.btnAccept.setGeometry(QtCore.QRect(80, 260, 113, 32))
        self.btnAccept.setCheckable(True)
        self.btnAccept.setObjectName("btnAccept")
        self.btnDeny = QtWidgets.QPushButton(phieunhap_dialog)
        self.btnDeny.setGeometry(QtCore.QRect(210, 260, 113, 32))
        self.btnDeny.setCheckable(True)
        self.btnDeny.setObjectName("btnDeny")
        self.label_3 = QtWidgets.QLabel(phieunhap_dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 91, 16))
        self.label_3.setObjectName("label_3")
        self.dateNgayTao = QtWidgets.QDateEdit(phieunhap_dialog)
        self.dateNgayTao.setGeometry(QtCore.QRect(170, 170, 181, 22))
        self.dateNgayTao.setObjectName("dateNgayTao")
        self.label_5 = QtWidgets.QLabel(phieunhap_dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 91, 16))
        self.label_5.setObjectName("label_5")
        self.cbMaNV = QtWidgets.QComboBox(phieunhap_dialog)
        self.cbMaNV.setGeometry(QtCore.QRect(170, 90, 181, 22))
        self.cbMaNV.setObjectName("cbMaNV")
        self.cbMaNCC = QtWidgets.QComboBox(phieunhap_dialog)
        self.cbMaNCC.setGeometry(QtCore.QRect(170, 130, 181, 22))
        self.cbMaNCC.setObjectName("cbMaNCC")
        self.btnDeny.toggled['bool'].connect(phieunhap_dialog.close)

        self.retranslateUi(phieunhap_dialog)
        QtCore.QMetaObject.connectSlotsByName(phieunhap_dialog)

    def retranslateUi(self, phieunhap_dialog):
        _translate = QtCore.QCoreApplication.translate
        phieunhap_dialog.setWindowTitle(_translate("phieunhap_dialog", "Dialog"))
        self.label.setText(_translate("phieunhap_dialog", "Mã nhân viên"))
        self.label_2.setText(_translate("phieunhap_dialog", "Mã nhà cung cấp"))
        self.label_4.setText(_translate("phieunhap_dialog", "THÊM PHIẾU NHẬP"))
        self.btnAccept.setText(_translate("phieunhap_dialog", "Xác nhận"))
        self.btnDeny.setText(_translate("phieunhap_dialog", "Huỷ"))
        self.label_3.setText(_translate("phieunhap_dialog", "Ngày lập"))
        self.label_5.setText(_translate("phieunhap_dialog", "Tổng tiền"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    phieunhap_dialog = QtWidgets.QDialog()
    ui = Ui_phieunhap_dialog()
    ui.setupUi(phieunhap_dialog)
    phieunhap_dialog.show()
    sys.exit(app.exec_())
