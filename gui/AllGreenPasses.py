# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AllGreenPasses.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import web3_interface

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
        self.create_table()

        self.retranslateUi(AllGreenPasses)
        QtCore.QMetaObject.connectSlotsByName(AllGreenPasses)

    def retranslateUi(self, AllGreenPasses):
        _translate = QtCore.QCoreApplication.translate
        AllGreenPasses.setWindowTitle(_translate("AllGreenPasses", "All Green Passes Status"))
        self.GreenPassesLabel.setText(_translate("AllGreenPasses", "<html><head/><body><p><span style=\" font-size:22pt; font-style:italic; text-decoration: underline;\">All Green Passes</span></p></body></html>"))
    
    def create_table(self):
        self.table = QtWidgets.QTableWidget(self.AllGreenPassesTable)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Name', 'ID', 'Expiration Date'])
        hheader = self.table.horizontalHeader()
        hheader.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        rows = web3_interface.get_all_greenpass()
        print(rows)
        self.table.setRowCount(len(rows))
        row_num = 0
        for row in rows:
            print(row)
            print(row[0])
            print(row[1])
            print(row[2])
            self.table.setItem(row_num, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.table.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.table.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            row_num += 1

        self.table.resizeColumnsToContents()
