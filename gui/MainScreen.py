# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from AddGreenPass import Ui_AddGreenPass
# from GetGreenPass import Ui_GetLicense
from RenewGreenPass import *
from AllGreenPasses import *
from GetGreenPass import *
import BackGround

class Ui_GreenPass(object):
    def openAddGreenPass(self):
        self.window=QtWidgets.QMainWindow()
        self.uiNew=Ui_AddGreenPass()
        self.uiNew.setupUi(self.window)
        self.window.show()

    def openGetGreenPass(self):
        self.window=QtWidgets.QMainWindow()
        self.uiNew=Ui_GetGreenPass()
        self.uiNew.setupUi(self.window)
        self.window.show()
    
    def openRenewGreenPass(self):
        self.window=QtWidgets.QMainWindow()
        self.uiNew=Ui_RenewGreenPass()
        self.uiNew.setupUi(self.window)
        self.window.show()
    
    def openAllGreenPass(self):
        self.window=QtWidgets.QMainWindow()
        self.uiNew=Ui_AllGreenPasses()
        self.uiNew.setupUi(self.window)
        self.window.show()

    def setupUi(self, GreenPass):
        GreenPass.setObjectName("GreenPass")
        GreenPass.resize(757, 518)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(GreenPass.sizePolicy().hasHeightForWidth())
        GreenPass.setSizePolicy(sizePolicy)
        GreenPass.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setUnderline(True)
        GreenPass.setFont(font)
        GreenPass.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        GreenPass.setMouseTracking(False)
        GreenPass.setWindowOpacity(14.0)
        GreenPass.setAutoFillBackground(False)
        GreenPass.setStyleSheet("border-image: url(:/GreenPass/Images/Background.jpg);\n"
"")
        GreenPass.setIconSize(QtCore.QSize(10, 24))
        self.widget = QtWidgets.QWidget(GreenPass)
        self.widget.setObjectName("widget")

        # ------------------------ADD GreenPass BUTTON------------------------
        self.AddGreenPass = QtWidgets.QPushButton(self.widget)
        self.AddGreenPass.setGeometry(QtCore.QRect(260, 30, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.AddGreenPass.setFont(font)
        self.AddGreenPass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddGreenPass.setAutoFillBackground(False)
        self.AddGreenPass.setStyleSheet("border-image: url(:/newPrefix/Images/WHITE.jpg);")
        self.AddGreenPass.setCheckable(False)
        self.AddGreenPass.setChecked(False)
        self.AddGreenPass.setAutoDefault(False)
        self.AddGreenPass.setObjectName("AddGreenPass")
        self.AddGreenPass.clicked.connect(self.openAddGreenPass)
        # ------------------------GET GreenPass BUTTON------------------------
        self.GetGreenPass = QtWidgets.QPushButton(self.widget)
        self.GetGreenPass.setGeometry(QtCore.QRect(260, 150, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.GetGreenPass.setFont(font)
        self.GetGreenPass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GetGreenPass.setStyleSheet("border-image: url(:/newPrefix/Images/WHITE.jpg);")
        self.GetGreenPass.setCheckable(False)
        self.GetGreenPass.setChecked(False)
        self.GetGreenPass.setObjectName("GetGreenPass")
        self.GetGreenPass.clicked.connect(self.openGetGreenPass)
        # ------------------------RENEW GreenPass BUTTON------------------------
        self.RenewGreenPass = QtWidgets.QPushButton(self.widget)
        self.RenewGreenPass.setGeometry(QtCore.QRect(260, 270, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.RenewGreenPass.setFont(font)
        self.RenewGreenPass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RenewGreenPass.setStyleSheet("border-image: url(:/newPrefix/Images/WHITE.jpg);")
        self.RenewGreenPass.setCheckable(False)
        self.RenewGreenPass.setChecked(False)
        self.RenewGreenPass.setObjectName("RenewGreenPass")
        self.RenewGreenPass.clicked.connect(self.openRenewGreenPass)
        # ------------------------All GreenPass BUTTON------------------------
        self.ShowAllGreenPass = QtWidgets.QPushButton(self.widget)
        self.ShowAllGreenPass.setGeometry(QtCore.QRect(260, 390, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.ShowAllGreenPass.setFont(font)
        self.ShowAllGreenPass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ShowAllGreenPass.setStyleSheet("border-image: url(:/newPrefix/Images/WHITE.jpg);")
        self.ShowAllGreenPass.setCheckable(False)
        self.ShowAllGreenPass.setChecked(False)
        self.ShowAllGreenPass.setObjectName("ShowAllGreenPass")
        GreenPass.setCentralWidget(self.widget)
        self.statusbar = QtWidgets.QStatusBar(GreenPass)
        self.statusbar.setObjectName("statusbar")
        self.ShowAllGreenPass.clicked.connect(self.openAllGreenPass)

        GreenPass.setStatusBar(self.statusbar)
        self.retranslateUi(GreenPass)
        QtCore.QMetaObject.connectSlotsByName(GreenPass)

    def retranslateUi(self, GreenPass):
        _translate = QtCore.QCoreApplication.translate
        GreenPass.setWindowTitle(_translate("GreenPass", "Green Pass"))
        self.AddGreenPass.setText(_translate("GreenPass", "Add Green Pass"))
        self.GetGreenPass.setText(_translate("GreenPass", "Get Green Pass"))
        self.RenewGreenPass.setText(_translate("GreenPass", "Renew Green Pass"))
        self.ShowAllGreenPass.setText(_translate("GreenPass", "All Green Passes"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GreenPassWidget = QtWidgets.QMainWindow()
    ui = Ui_GreenPass()
    ui.setupUi(GreenPassWidget)
    GreenPassWidget.show()

    sys.exit(app.exec_())
