# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ErrorMessage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(442, 207)
        Error.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Error.setStyleSheet("background-color: rgb(98, 203, 255);")
        self.pushButton = QtWidgets.QPushButton(Error)
        self.pushButton.setGeometry(QtCore.QRect(160, 140, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.ErrorMsg = QtWidgets.QLabel(Error)
        self.ErrorMsg.setGeometry(QtCore.QRect(50, 10, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorMsg.setFont(font)
        self.ErrorMsg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ErrorMsg.setAutoFillBackground(False)
        self.ErrorMsg.setObjectName("ErrorMsg")

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Error!"))
        self.pushButton.setText(_translate("Error", "Close"))
        self.ErrorMsg.setText(_translate("Error", "You don\'t have the permission\n"
"         to add a green pass"))