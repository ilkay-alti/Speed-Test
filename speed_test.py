# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 210, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 50, 67, 17))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 70, 81, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 90, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 150, 111, 41))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.ping = QtWidgets.QLabel(Dialog)
        self.ping.setGeometry(QtCore.QRect(190, 50, 121, 17))
        self.ping.setText("")
        self.ping.setObjectName("ping")
        self.down_load = QtWidgets.QLabel(Dialog)
        self.down_load.setGeometry(QtCore.QRect(190, 70, 101, 17))
        self.down_load.setText("")
        self.down_load.setObjectName("down_load")
        self.up_load = QtWidgets.QLabel(Dialog)
        self.up_load.setGeometry(QtCore.QRect(190, 90, 141, 17))
        self.up_load.setText("")
        self.up_load.setObjectName("up_load")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "START"))
        self.label.setText(_translate("Dialog", "Ping :"))
        self.label_4.setText(_translate("Dialog", "Download"))
        self.label_5.setText(_translate("Dialog", "Upload"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
