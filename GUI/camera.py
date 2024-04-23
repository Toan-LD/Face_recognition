# Dialog implementation generated from reading ui file 'ui/camera.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap,QImage
from trainModel import CNNModel
import numpy as np
import cv2

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import GUI.thongbao as tb


class Ui_Form(object):
    def setupUi(self, Dialog, id, type=1):
        #Khai báo
        self.tb = tb.Ui_Dialog()
        self.id = id
        self.type=type
        self.data_dir = 'data/khachhang'
        self.parent_directory = f'data/khachhang/{id}'
        self.Dialog = Dialog
        self.count = 0
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 550)
        Dialog.setMaximumSize(QtCore.QSize(900, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 510))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        #Chạy tiến trình lưu ảnh
        self.btnStart = QtWidgets.QPushButton(parent=Dialog)
        self.btnStart.setMinimumSize(QtCore.QSize(180, 30))
        self.btnStart.setMaximumSize(QtCore.QSize(180, 30))
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnStart.clicked.connect(self.start_capture)
        
        #Tắt camera
        self.btnClose = QtWidgets.QPushButton(parent=Dialog)
        self.btnClose.setMinimumSize(QtCore.QSize(180, 30))
        self.btnClose.setMaximumSize(QtCore.QSize(180, 30))
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.btnClose.clicked.connect(self.close_dialog)
        
        #Xoá ảnh trong kho lưu trữ
        self.btnDelete = QtWidgets.QPushButton(parent=Dialog)
        self.btnDelete.setMinimumSize(QtCore.QSize(180, 30))
        self.btnDelete.setMaximumSize(QtCore.QSize(180, 30))
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnDelete.clicked.connect(self.delete_directory)
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.camera = cv2.VideoCapture(1)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(50)
        
        self.timer_capture = QTimer()
        self.timer_capture.timeout.connect(self.chup_anh)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        if self.type == 2:
            self.data_dir = 'data/thunuoi'
            self.parent_directory = f'data/thunuoi/{id}'

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnStart.setText(_translate("Dialog", "Bắt đầu"))
        self.btnClose.setText(_translate("Dialog", "Đóng"))
        self.btnDelete.setText(_translate("Dialog", "Xoá dữ liệu"))

    def update_frame(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        ret, frame = self.camera.read()
        if ret:
            # Chuyển đổi hình ảnh từ BGR sang RGB để hiển thị trong PyQt5
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb = cv2.resize(frame_rgb,(900,600))
            
            self.faces = self.face_cascade.detectMultiScale(frame_rgb, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            if self.type == 1:
                for (x, y, w, h) in self.faces:
                    cv2.rectangle(frame_rgb, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            image = QImage(frame_rgb.data, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            
            self.label.setPixmap(pixmap)
    

    def start_capture(self):
        # Bắt đầu lập lịch chụp ảnh bằng cách bật QTimer
        self.timer_capture.start(200)
            
    def chup_anh(self):
        self.btnStart.setText("Đang lưu ảnh....!")
        ret , frame = self.camera.read()
        self.check_directory()
        if ret:
            self.faces = self.face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            if len(self.faces) !=0:
                if self.count >= 30:
                    if self.type == 1:
                        self.tb.thongBao("Đã lưu dữ liệu gương mặt hoàn tất!")
                    else: 
                        self.tb.thongBao("Đã lưu dữ liệu thú nuôi hoàn tất!")
                    self.count= 0
                    self.timer_capture.stop()
                    self.btnStart.setText("Bắt đầu")
                    self.trainModel(self.data_dir)
                elif(self.type == 1):
                    for (x, y, w, h) in self.faces:
                        face_image = frame[y:y+h, x:x+w]
                        self.save_pic(face_image)
                else:
                    self.save_pic(frame)
    
    def trainModel(self,data_dir):
        list = os.listdir(data_dir)
        num = len(list)
        model = CNNModel(num_class=num)
        datax, datay = model.load_data(data_dir)
        model.train_model(datax, datay)
        if self.type == 1:
            model.save_model("model/modelKH.h5")
        else:
            model.save_model("model/modelTN.h5")
                    
                        
            
        
    def check_directory(self):
        if not os.path.exists(self.parent_directory):
                os.makedirs(self.parent_directory)  
    
    def save_pic(self,face_image):
        alpha = 1.5  # Độ sáng
        beta = 30   # Độ tương phản
        adjusted_image = cv2.convertScaleAbs(face_image, alpha=alpha, beta=beta)

        # Phóng to và thu nhỏ
        scaled_up_image = cv2.resize(face_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
        scaled_down_image = cv2.resize(face_image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

        # Quay ảnh
        rows, cols = face_image.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)  # Quay góc 45 độ
        rotated_image = cv2.warpAffine(face_image, rotation_matrix, (cols, rows))

        # Làm mờ và làm nổi bật
        blurred_image = cv2.GaussianBlur(face_image, (9, 9), 0)
        sharpened_image = cv2.filter2D(face_image, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))

        cv2.imwrite(f'{self.parent_directory}/{self.id}_{self.count}.png',face_image)
        cv2.imwrite(f'{self.parent_directory}/{self.id}_adjusted_{self.count}.png',adjusted_image)
        cv2.imwrite(f'{self.parent_directory}/{self.id}_up_{self.count}.png',scaled_up_image)
        cv2.imwrite(f'{self.parent_directory}/{self.id}_down_{self.count}.png',scaled_down_image)
        cv2.imwrite(f'{self.parent_directory}/{self.id}_rotated_{self.count}.png',rotated_image)
        cv2.imwrite(f'{self.parent_directory}/{self.id}_blurred_{self.count}.png',blurred_image)
        cv2.imwrite(f'{self.parent_directory}/{self.id}_sharpened_{self.count}.png',sharpened_image)
        self.count += 1 
    
    def close_dialog(self):
        self.camera.release()
        self.Dialog.close()
        
    def delete_directory(self):
        try:
            os.remove(self.parent_directory)
            self.tb.thongBao("Đã xoá thư mục thành công !")
        except OSError as e:
            self.tb.thongBao(f"Lỗi: {self.parent_directory} - {e.strerror}")
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog,4)
    Dialog.show()
    sys.exit(app.exec())
