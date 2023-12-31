# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def openWindow(self,error_message):
        _translate = QtCore.QCoreApplication.translate
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.errorMessage.setText(_translate("Dialog", error_message))
        self.window.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(357, 143)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.errorMessage = QtWidgets.QLabel(Dialog)
        self.errorMessage.setGeometry(QtCore.QRect(30, 60, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.errorMessage.setFont(font)
        self.errorMessage.setObjectName("errorMessage")
        self.okButton = QtWidgets.QPushButton(Dialog,clicked=lambda:self.closewindow(Dialog))
        self.okButton.setGeometry(QtCore.QRect(270, 110, 75, 23))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def closewindow(self,Dialog):
        self.dialog=Dialog
        self.dialog.close()
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Error"))
        self.errorMessage.setText(_translate("Dialog", "Error Message"))
        self.okButton.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
