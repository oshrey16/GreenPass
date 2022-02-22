# # -*- coding: utf-8 -*-

# # Form implementation generated from reading ui file 'AddGreenPass.ui'
# #
# # Created by: PyQt5 UI code generator 5.9.2
# #
# # WARNING! All changes made in this file will be lost!

# from datetime import datetime, date
# from ErrorMessage import *
# import web3_interface
# from PyQt5 import QtCore, QtGui, QtWidgets

# class Ui_AddGreenPass(object):
#     def setupUi(self, AddGreenPass):
#         AddGreenPass.setObjectName("AddGreenPass")
#         AddGreenPass.resize(499, 362)
#         AddGreenPass.setStyleSheet("background-color: rgb(98, 203, 255);")
#         self.fNameInput = QtWidgets.QLineEdit(AddGreenPass)
#         self.fNameInput.setGeometry(QtCore.QRect(200, 90, 171, 21))
#         self.fNameInput.setObjectName("fNameInput")
#         self.LNameInput = QtWidgets.QLineEdit(AddGreenPass)
#         self.LNameInput.setGeometry(QtCore.QRect(200, 150, 171, 21))
#         self.LNameInput.setObjectName("LNameInput")
#         self.exprInput = QtWidgets.QLineEdit(AddGreenPass)
#         self.exprInput.setGeometry(QtCore.QRect(230, 210, 171, 21))
#         self.exprInput.setTabletTracking(False)
#         self.exprInput.setObjectName("exprInput")
#         self.FirstName = QtWidgets.QLabel(AddGreenPass)
#         self.FirstName.setGeometry(QtCore.QRect(60, 90, 131, 16))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.FirstName.setFont(font)
#         self.FirstName.setObjectName("FirstName")
#         self.LastName = QtWidgets.QLabel(AddGreenPass)
#         self.LastName.setGeometry(QtCore.QRect(60, 150, 131, 16))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.LastName.setFont(font)
#         self.LastName.setObjectName("LastName")
#         self.ExprDate = QtWidgets.QLabel(AddGreenPass)
#         self.ExprDate.setGeometry(QtCore.QRect(40, 210, 181, 21))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.ExprDate.setFont(font)
#         self.ExprDate.setObjectName("ExprDate")
#         self.DeployBttn = QtWidgets.QPushButton(AddGreenPass)
#         self.DeployBttn.setGeometry(QtCore.QRect(170, 280, 171, 51))
#         font = QtGui.QFont()
#         font.setPointSize(11)
#         font.setBold(True)
#         font.setItalic(False)
#         font.setUnderline(False)
#         font.setWeight(75)
#         self.DeployBttn.setFont(font)
#         self.DeployBttn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.DeployBttn.setObjectName("DeployBttn")
#         self.DeployBttn.clicked.connect(self.addGreenPass)
#         self.Id = QtWidgets.QLabel(AddGreenPass)
#         self.Id.setGeometry(QtCore.QRect(120, 30, 101, 16))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.Id.setFont(font)
#         self.Id.setObjectName("Id")
#         self.exprInput_2 = QtWidgets.QLineEdit(AddGreenPass)
#         self.exprInput_2.setGeometry(QtCore.QRect(170, 30, 171, 21))
#         self.exprInput_2.setObjectName("exprInput_2")

#         self.retranslateUi(AddGreenPass)
#         QtCore.QMetaObject.connectSlotsByName(AddGreenPass)

#     def retranslateUi(self, AddGreenPass):
#         _translate = QtCore.QCoreApplication.translate
#         AddGreenPass.setWindowTitle(_translate("AddGreenPass", "Add Green Pass"))
#         self.FirstName.setText(_translate("AddGreenPass", "First Name :"))
#         self.LastName.setText(_translate("AddGreenPass", "Last Name :"))
#         self.ExprDate.setText(_translate("AddGreenPass", "Experation Date :"))
#         self.DeployBttn.setText(_translate("AddGreenPass", "Deploy"))
#         self.Id.setText(_translate("AddGreenPass", "ID :"))
    
#     def set_expiration(self, _date):
#         global expiration_date
#         print(f'{_date}')
#         now = datetime.now()
#         now = date(now.year, now.month, now.day)
#         selected = date(_date.year(), _date.month(), _date.day())
#         print(f'now = {now}\n'
#               f'selected = {selected}')
#         expiration_date = (selected - now).days
#         print(f'expiration: {expiration_date}')
    
#     def ErrorMsg(self):
#         self.window = QtWidgets.QMainWindow()
#         self.uiNew = Ui_Error()
#         self.uiNew.setupUi(self.window)
#         self.window.show()

#     def addGreenPass(self):
#         fname = self.fNameInput.text()
#         lname = self.LNameInput.text()
#         id = self.exprInput_2.text()
#         web3_interface.add_green_pass(fname, lname, id, expiration_date)

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddGreenPass.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from datetime import datetime, date
from ErrorMessage import *
import web3_interface
from PyQt5 import QtCore, QtGui, QtWidgets
expiration_date = 0

class Ui_AddGreenPass(object):
    def setupUi(self, AddGreenPass):
        AddGreenPass.setObjectName("AddGreenPass")
        AddGreenPass.resize(499, 698)
        AddGreenPass.setStyleSheet("background-color: rgb(98, 203, 255);")
        self.fNameInput = QtWidgets.QLineEdit(AddGreenPass)
        self.fNameInput.setGeometry(QtCore.QRect(200, 90, 171, 21))
        self.fNameInput.setObjectName("fNameInput")
        self.LNameInput = QtWidgets.QLineEdit(AddGreenPass)
        self.LNameInput.setGeometry(QtCore.QRect(200, 150, 171, 21))
        self.LNameInput.setObjectName("LNameInput")
        self.FirstName = QtWidgets.QLabel(AddGreenPass)
        self.FirstName.setGeometry(QtCore.QRect(60, 90, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FirstName.setFont(font)
        self.FirstName.setObjectName("FirstName")
        self.LastName = QtWidgets.QLabel(AddGreenPass)
        self.LastName.setGeometry(QtCore.QRect(60, 150, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LastName.setFont(font)
        self.LastName.setObjectName("LastName")
        self.ExprDate = QtWidgets.QLabel(AddGreenPass)
        self.ExprDate.setGeometry(QtCore.QRect(50, 210, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ExprDate.setFont(font)
        self.ExprDate.setObjectName("ExprDate")
        self.DeployBttn = QtWidgets.QPushButton(AddGreenPass)
        self.DeployBttn.setGeometry(QtCore.QRect(170, 600, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.DeployBttn.setFont(font)
        self.DeployBttn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DeployBttn.setObjectName("DeployBttn")
        self.DeployBttn.clicked.connect(self.addGreenPass)
        self.ExprDate_2 = QtWidgets.QLabel(AddGreenPass)
        self.ExprDate_2.setGeometry(QtCore.QRect(120, 30, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ExprDate_2.setFont(font)
        self.ExprDate_2.setObjectName("ExprDate_2")
        self.exprInput_2 = QtWidgets.QLineEdit(AddGreenPass)
        self.exprInput_2.setGeometry(QtCore.QRect(170, 30, 171, 21))
        self.exprInput_2.setObjectName("exprInput_2")

        current_month = datetime.now().month
        current_year = datetime.now().year
        self.calendarWidget = QtWidgets.QCalendarWidget(AddGreenPass)
        self.calendarWidget.setMinimumDate(QtCore.QDate(current_year, current_month + 6, 1))
        self.calendarWidget.setGeometry(QtCore.QRect(40, 250, 421, 291))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.clicked.connect(self.set_expiration)
        self.retranslateUi(AddGreenPass)
        QtCore.QMetaObject.connectSlotsByName(AddGreenPass)

    def retranslateUi(self, AddGreenPass):
        _translate = QtCore.QCoreApplication.translate
        AddGreenPass.setWindowTitle(_translate("AddGreenPass", "Add Green Pass"))
        self.FirstName.setText(_translate("AddGreenPass", "First Name :"))
        self.LastName.setText(_translate("AddGreenPass", "Last Name :"))
        self.ExprDate.setText(_translate("AddGreenPass", "Experation Date :"))
        self.DeployBttn.setText(_translate("AddGreenPass", "Deploy"))
        self.ExprDate_2.setText(_translate("AddGreenPass", "ID :"))

    def set_expiration(self, _date):
        global expiration_date
        print(f'{_date}')
        now = datetime.now()
        now = date(now.year, now.month, now.day)
        selected = date(_date.year(), _date.month(), _date.day())
        print(f'now = {now}\n'
              f'selected = {selected}')
        expiration_date = (selected - now).days
        print(f'expiration: {expiration_date}')
    
    def ErrorMsg(self):
        self.window = QtWidgets.QMainWindow()
        self.uiNew = Ui_Error()
        self.uiNew.setupUi(self.window)
        self.window.show()

    def addGreenPass(self):
        print("PARAMETERS:")
        fname = self.fNameInput.text()
        lname = self.LNameInput.text()
        id = self.exprInput_2.text()
        id = int(id)
        print(fname,lname,id,expiration_date)
        web3_interface.add_green_pass(fname, lname, id, expiration_date)
