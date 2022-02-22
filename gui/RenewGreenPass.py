# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RenewGreenPass.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import web3_interface
from datetime import datetime, date

class Ui_RenewGreenPass(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 246)
        Form.setStyleSheet("background-color: rgb(98, 203, 255);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 110, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.pushButton.setObjectName("pushButton")
        self.enterID = QtWidgets.QLineEdit(Form)
        self.enterID.setGeometry(QtCore.QRect(210, 40, 231, 31))
        self.enterID.setStyleSheet("font: 11pt \"Calibri\";")
        self.enterID.setText("")
        self.enterID.setObjectName("enterID")
        self.ID = QtWidgets.QLabel(Form)
        self.ID.setGeometry(QtCore.QRect(130, 40, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ID.setFont(font)
        self.ID.setObjectName("ID")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RenewGreenPass"))
        self.pushButton.setText(_translate("Form", "Deploy"))
        self.ID.setText(_translate("Form", "ID :"))
    

    expiration_date = 0
    def set_expiration(_date):
        global expiration_date
        print(f'{_date}')
        now = datetime.now()
        now = date(now.year, now.month, now.day)
        selected = date(_date.year(), _date.month(), _date.day())
        print(f'now = {now}\n'
              f'selected = {selected}')
        expiration_date = (selected - now).days
        print(f'expiration: {expiration_date}')

    def renewGreenPass(self):
        id = self.enterID.text()
        id = int(id)
        web3_interface.renew_green_pass(id)