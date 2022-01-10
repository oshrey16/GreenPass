# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AllGreenPasses.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AllGreenPasses(object):
    def setupUi(self, AllGreenPasses):
        AllGreenPasses.setObjectName("AllGreenPasses")
        AllGreenPasses.resize(647, 484)
        AllGreenPasses.setStyleSheet("background-color: rgb(98, 203, 255);")
        self.AllGreenPassesTable = QtWidgets.QListView(AllGreenPasses)
        self.AllGreenPassesTable.setEnabled(False)
        self.AllGreenPassesTable.setGeometry(QtCore.QRect(10, 110, 631, 361))
        self.AllGreenPassesTable.setObjectName("AllGreenPassesTable")
        self.GreenPassesLabel = QtWidgets.QLabel(AllGreenPasses)
        self.GreenPassesLabel.setGeometry(QtCore.QRect(190, 30, 281, 71))
        self.GreenPassesLabel.setObjectName("GreenPassesLabel")

        self.retranslateUi(AllGreenPasses)
        QtCore.QMetaObject.connectSlotsByName(AllGreenPasses)

    def retranslateUi(self, AllGreenPasses):
        _translate = QtCore.QCoreApplication.translate
        AllGreenPasses.setWindowTitle(_translate("AllGreenPasses", "All Green Passes Status"))
        self.GreenPassesLabel.setText(_translate("AllGreenPasses", "<html><head/><body><p><span style=\" font-size:22pt; font-style:italic; text-decoration: underline;\">All Green Passes</span></p></body></html>"))

