# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetGreenPass.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import web3_interface
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GetGreenPass(object):
    def button_clicked(self):
        print("BUTTON CLICKED!!!!!!!!!!!")
        id = self.ID_2.text()
        print(id)
        green_pass = web3_interface.get_single_greenpass(int(id))
        green_pass_visual = f'Name:\t\t{green_pass[0]}\nID:\t\t{green_pass[1]}\nExpiration Date:\t{green_pass[2]}'
        # self.green_pass.setText(green_pass_visual)
        self.ExpirationDate.setText(str(green_pass[2]))
    
    def setupUi(self, GetGreenPass):
        GetGreenPass.setObjectName("GetGreenPass")
        GetGreenPass.resize(608, 392)
        GetGreenPass.setStyleSheet("background-color: rgb(98, 203, 255);")
        self.ID_2 = QtWidgets.QLineEdit(GetGreenPass)
        self.ID_2.setGeometry(QtCore.QRect(230, 80, 171, 31))
        self.ID_2.setStyleSheet("font: 11pt \"Calibri\";")
        self.ID_2.setText("")
        self.ID_2.setObjectName("ID_2")
        self.ID = QtWidgets.QLabel(GetGreenPass)
        self.ID.setGeometry(QtCore.QRect(230, 60, 131, 21))
        self.ID.setObjectName("ID")
        self.CheckBttn = QtWidgets.QPushButton(GetGreenPass)
        self.CheckBttn.setGeometry(QtCore.QRect(260, 130, 93, 28))
        self.CheckBttn.setObjectName("CheckBttn")
        self.CheckBttn.clicked.connect(self.button_clicked)
        self.ExpirationDate = QtWidgets.QLabel(GetGreenPass)
        # self.ExpirationDate = QtWidgets.QGraphicsView(GetGreenPass)
        self.ExpirationDate.setGeometry(QtCore.QRect(170, 250, 256, 31))
        self.ExpirationDate.setObjectName("ExpirationDate")
        self.label = QtWidgets.QLabel(GetGreenPass)
        self.label.setGeometry(QtCore.QRect(180, 220, 151, 16))
        self.label.setObjectName("label")

        self.retranslateUi(GetGreenPass)
        QtCore.QMetaObject.connectSlotsByName(GetGreenPass)

    def retranslateUi(self, GetGreenPass):
        _translate = QtCore.QCoreApplication.translate
        GetGreenPass.setWindowTitle(_translate("GetGreenPass", "Get Green Pass"))
        self.ID.setText(_translate("GetGreenPass", "ID :"))
        self.CheckBttn.setText(_translate("GetGreenPass", "Check"))
        self.label.setText(_translate("GetGreenPass", "Your Exiration Date is:"))

