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
        self.__kp = 250
        self.__ki = 260
        self.__kd = 90
        self.__ti = 0.01
        self.__td = 0.01

        self._kp = 0.0
        self._ki = 0.0
        self._kd = 0.0
        self._ti = 0.0
        self._td = 0.0

        self._updateornot = False

    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        # Dialog.resize(537, 386)
        Dialog.resize(440, 500)

        # steer_angle, speed, control blocks
        self.kp_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.kp_box.setGeometry(QtCore.QRect(50, 60, 80, 40))
        self.kp_box.setObjectName("kp_box")
        self.kp_box.valueChanged.connect(self.kp)
        self.kp_box.setRange(0, 2000)
        self.kp_box.setValue(self.__kp)

        self.ki_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.ki_box.setGeometry(QtCore.QRect(182, 60, 80, 40))
        self.ki_box.setObjectName("ki_box")
        self.ki_box.valueChanged.connect(self.ki)
        self.ki_box.setRange(0, 100000)
        self.ki_box.setSingleStep(1)
        self.ki_box.setValue(self.__ki)

        self.kd_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.kd_box.setGeometry(QtCore.QRect(310, 60, 80, 40))
        self.kd_box.setObjectName("kd_box")
        self.kd_box.valueChanged.connect(self.kd)
        self.kd_box.setRange(0, 1000)
        self.kd_box.setValue(self.__kd)

        self.ti_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.ti_box.setGeometry(QtCore.QRect(50, 160, 100, 40))
        self.ti_box.setObjectName("ti_box")
        self.ti_box.valueChanged.connect(self.ti)
        self.ti_box.setRange(0, 3)
        self.ti_box.setSingleStep(0.0005)
        self.ti_box.setDecimals(5)
        self.ti_box.setValue(self.__ti)

        self.td_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.td_box.setGeometry(QtCore.QRect(290, 160, 100, 40))
        self.td_box.setObjectName("td_box")
        self.td_box.valueChanged.connect(self.td)
        self.td_box.setRange(0, 3)
        self.td_box.setSingleStep(0.0005)
        self.td_box.setDecimals(5)
        self.td_box.setValue(self.__td)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 85, 20))
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(182, 40, 85, 20))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 40, 85, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 85, 20))
        self.label_3.setObjectName("label_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(300, 140, 85, 20))
        self.label_4.setObjectName("label_4")

        self.author_tag = QtWidgets.QLabel(Dialog)
        self.author_tag.setGeometry(QtCore.QRect(330, 450, 130, 45))
        self.author_tag.setObjectName("author_tag")

        self.find_kid_cmd = QtWidgets.QPushButton(Dialog)
        self.find_kid_cmd.setGeometry(QtCore.QRect(60, 380, 120, 35))
        self.find_kid_cmd.setObjectName("find_kid")
        self.find_kid_cmd.setDefault(False)
        self.find_kid_cmd.setAutoDefault(False)
        self.find_kid_cmd.clicked.connect(self.find_kid)

        self.find_tid_cmd = QtWidgets.QPushButton(Dialog)
        self.find_tid_cmd.setGeometry(QtCore.QRect(260, 380, 120, 35))
        self.find_tid_cmd.setObjectName("find_tid")
        self.find_tid_cmd.setDefault(False)
        self.find_tid_cmd.setAutoDefault(False)
        self.find_tid_cmd.clicked.connect(self.find_tid)

        self.update_data_cmd = QtWidgets.QPushButton(Dialog)
        self.update_data_cmd.setGeometry(QtCore.QRect(160, 430, 120, 35))
        self.update_data_cmd.setObjectName("set_enable")
        self.update_data_cmd.setDefault(False)
        self.update_data_cmd.setAutoDefault(False)
        self.update_data_cmd.clicked.connect(self.set_enable)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def kp(self):
        self._kp = self.kp_box.value()
        # print(f"The new Kp gain is set to {self.kp_box.value()}")

    def ki(self):
        self._ki = self.ki_box.value()
        # print(f"The new Ki gain is set to {self.ki_box.value()}")

    def kd(self):
        self._kd = self.kd_box.value()
        # print(f"The new Kd gain is set to {self.kd_box.value()}")

    def ti(self):
        self._ti = self.ti_box.value()
        # print(f"The new Ti time is set to {self.ti_box.value()}")

    def td(self):
        self._td = self.td_box.value()
        # print(f"The new Td time is set to {self.td_box.value()}")

    def find_kid(self):
        """return the Ki and Kd based on Ti and Td inputs."""
        if self._updateornot:
            if self._ti == 0:
                self._ki = 0
            else:
                self._ki = self._kp / self._ti / 60.0
            self._kd = self._kp * self._td * 60
            self.ki_box.setValue(self._ki)
            self.kd_box.setValue(self._kd)
            print("Press the Enable button again to make this button enabled!")
            self.find_kid_cmd.setEnabled(False)
            self.find_tid_cmd.setEnabled(False)
            self.find_kid_cmd.setStyleSheet("background-color : rgb(169, 169, 169)")
            self.find_tid_cmd.setStyleSheet("background-color : rgb(169, 169, 169)")

    def find_tid(self):
        """return the Ti and Td based on Ki and Kd inputs."""
        if self._updateornot:
            if self._ki == 0:
                self._ti = 0
            else:
                self._ti = self._kp / self._ki / 60.0
            self._td = self._kd / self._kp / 60.0
            self.ti_box.setValue(self._ti)
            self.td_box.setValue(self._td)
            self._updateornot = False
            print("Press the Enable button again to make this button enabled!")
            self.find_kid_cmd.setEnabled(False)
            self.find_tid_cmd.setEnabled(False)
            self.find_kid_cmd.setStyleSheet("background-color : rgb(169, 169, 169)")
            self.find_tid_cmd.setStyleSheet("background-color : rgb(169, 169, 169)")

    def set_enable(self):
        self._updateornot = True
        self.find_kid_cmd.setStyleSheet("background-color : rgb(27, 232, 136)")
        self.find_tid_cmd.setStyleSheet("background-color : rgb(27, 232, 136)")
        self.find_kid_cmd.setEnabled(True)
        self.find_tid_cmd.setEnabled(True)

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
        self.author_tag.setText(_translate("Dialog", "Created:\nBob(Yang) W.\n@ U of Waterloo"))
        self.update_data_cmd.setText(_translate("Dialog", "Enable Buttons"))
        self.find_kid_cmd.setText(_translate("Dialog", "Find Ki and Kd"))
        self.find_tid_cmd.setText(_translate("Dialog", "Find Ti and Td"))
        self.update_data_cmd.setStyleSheet("background-color : rgb(27, 232, 136)")
        self.find_kid_cmd.setStyleSheet("background-color : rgb(169, 169, 169)")
        self.find_tid_cmd.setStyleSheet("background-color : rgb(169, 169, 169)")
        self.find_kid_cmd.setEnabled(False)
        self.find_tid_cmd.setEnabled(False)
        self.label.setStyleSheet("color : blue")
        self.label_1.setStyleSheet("color : blue")
        self.label_2.setStyleSheet("color : blue")
        self.label_3.setStyleSheet("color : red")
        self.label_4.setStyleSheet("color : red")
        self.author_tag.setStyleSheet("color : black")

        self.author_tag.setWordWrap(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    diag = QtWidgets.QDialog()
    gallery = Ui_Dialog()
    gallery.setup_ui(diag)
    diag.show()
    sys.exit(app.exec_())
