#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a small GUI for convert the PID parameters, using Kp value
    Author: Yang Wang @ U of Waterloo Maglev lab
    Created: Mon 13 Jun 2022 01:37:24 PM EDT
    Modification: N/A
    Version: final"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    """
    This is the ui dialog for the GUI
    """

    def __init__(self):
        self.__kp = 100
        self.__ki = 0.01
        self.__kd = 0.01
        self.__ti = 0.01
        self.__td = 0.01

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        # Dialog.resize(537, 386)
        Dialog.resize(480, 500)

        # steer_angle, speed, control blocks
        self.kp_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.kp_box.setGeometry(QtCore.QRect(50, 60, 80, 40))
        self.kp_box.setObjectName("kp_box")
        self.kp_box.valueChanged.connect(self.kp)
        self.kp_box.setRange(0, 400)
        self.kp_box.setValue(100)

        self.ki_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.ki_box.setGeometry(QtCore.QRect(185, 60, 80, 40))
        self.ki_box.setObjectName("ki_box")
        self.ki_box.valueChanged.connect(self.ki)
        self.ki_box.setRange(0, 1000000)
        self.ki_box.setSingleStep(1)
        self.ki_box.setValue(1000)

        self.kd_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.kd_box.setGeometry(QtCore.QRect(310, 60, 80, 40))
        self.kd_box.setObjectName("kd_box")
        self.kd_box.valueChanged.connect(self.kd)
        self.kd_box.setRange(0, 100)
        self.kd_box.setValue(1)

        self.ti_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.ti_box.setGeometry(QtCore.QRect(50, 160, 100, 40))
        self.ti_box.setObjectName("ti_box")
        self.ti_box.valueChanged.connect(self.ti)
        self.ti_box.setRange(0, 3)
        self.ti_box.setSingleStep(0.0005)
        self.ti_box.setDecimals(5)
        self.ti_box.setValue(0.01)

        self.td_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.td_box.setGeometry(QtCore.QRect(290, 160, 100, 40))
        self.td_box.setObjectName("td_box")
        self.td_box.valueChanged.connect(self.td)
        self.td_box.setRange(0, 3)
        self.td_box.setSingleStep(0.0005)
        self.td_box.setDecimals(5)
        self.td_box.setValue(0.01)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 75, 20))
        self.label.setObjectName("label")  # angle
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(185, 40, 85, 20))
        self.label_1.setObjectName("label_1")  # speed
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 40, 85, 20))
        self.label_2.setObjectName("label_2")  # angle_incre
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 85, 20))
        self.label_3.setObjectName("label_4")  # speed_incre
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(300, 140, 85, 20))
        self.label_4.setObjectName("label_4")  # speed_incre

        self.find_kid_cmd = QtWidgets.QPushButton(Dialog)
        self.find_kid_cmd.setGeometry(QtCore.QRect(60, 380, 120, 35))
        self.find_kid_cmd.setObjectName("find_kid")
        self.find_kid_cmd.setDefault(False)
        self.find_kid_cmd.clicked.connect(self.find_kid)

        self.find_tid_cmd = QtWidgets.QPushButton(Dialog)
        self.find_tid_cmd.setGeometry(QtCore.QRect(260, 380, 120, 35))
        self.find_tid_cmd.setObjectName("find_tid")
        self.find_tid_cmd.setDefault(False)
        self.find_tid_cmd.clicked.connect(self.find_tid)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def kp(self):
        print(f"The new Kp gain is set to {self.kp_box.value()}")

    def ki(self):
        print(f"The new Ki gain is set to {self.ki_box.value()}")

    def kd(self):
        print(f"The new Kd gain is set to {self.kd_box.value()}")

    def ti(self):
        print(f"The new Ti time is set to {self.ti_box.value()}")

    def td(self):
        print(f"The new Td time is set to {self.td_box.value()}")

    def find_kid(self):
        if self.ti_box.value() == 0:
            self.ki_box.setValue(0.0)
        else:
            self.ki_box.setValue(self.kp_box.value() / self.ti_box.value() / 60.0)
        self.kd_box.setValue(self.kp_box.value() * self.td_box.value() * 60.0)

    def find_tid(self):
        if self.ki_box.value() == 0:
            self.ti_box.setValue(0.0)
        else:
            self.ti_box.setValue(self.kp_box.value() / self.ki_box.value() / 60.0)
        self.td_box.setValue(self.kd_box.value() / self.kp_box.value() / 60.0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate(
            "Dialog", "PID Parameter Converter Tool"))
        # Dialog.setStyleSheet()
        self.label.setText(_translate("Dialog", "Kp in N/m"))
        self.label_1.setText(_translate("Dialog", "Ki in N/(m*s)"))
        self.label_2.setText(_translate("Dialog", "Kd in N*s/m"))
        self.label_3.setText(_translate("Dialog", "Ti in min"))
        self.label_4.setText(_translate("Dialog", "Td in min"))
        self.find_kid_cmd.setText(_translate("Dialog", "Find Ki and Kd"))
        self.find_kid_cmd.setStyleSheet("background-color : rgb(27, 232, 136)")
        self.find_tid_cmd.setText(_translate("Dialog", "Find Ti and Td"))
        self.find_tid_cmd.setStyleSheet("background-color : rgb(27, 232, 136)")
        self.label.setStyleSheet("color : blue")
        self.label_1.setStyleSheet("color : blue")
        self.label_2.setStyleSheet("color : blue")
        self.label_3.setStyleSheet("color : red")
        self.label_4.setStyleSheet("color : red")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    diag = QtWidgets.QDialog()
    gallery = Ui_Dialog()
    gallery.setupUi(diag)
    diag.show()
    sys.exit(app.exec_())
