# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dedilak.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DEDILAK2(object):
    def setupUi(self, DEDILAK2):
        DEDILAK2.setObjectName("DEDILAK2")
        DEDILAK2.resize(400, 300)
        DEDILAK2.setMaximumSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        DEDILAK2.setFont(font)
        self.pushButton = QtWidgets.QPushButton(DEDILAK2)
        self.pushButton.setGeometry(QtCore.QRect(130, 210, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(DEDILAK2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 371, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout.addWidget(self.checkBox_4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.gridLayoutWidget = QtWidgets.QWidget(DEDILAK2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 100, 371, 95))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setMaximumSize(QtCore.QSize(70, 60))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.retranslateUi(DEDILAK2)
        QtCore.QMetaObject.connectSlotsByName(DEDILAK2)

    def retranslateUi(self, DEDILAK2):
        _translate = QtCore.QCoreApplication.translate
        DEDILAK2.setWindowTitle(_translate("DEDILAK2", "Dialog"))
        self.pushButton.setText(_translate("DEDILAK2", "ПЕРЕЗАГРУЗКА"))
        self.checkBox.setText(_translate("DEDILAK2", "ВЫХОД 1"))
        self.checkBox_3.setText(_translate("DEDILAK2", "ВЫХОД 2"))
        self.checkBox_4.setText(_translate("DEDILAK2", "ВЫХОД 3"))
        self.checkBox_2.setText(_translate("DEDILAK2", "ВЫХОД 4"))
        self.label.setText(_translate("DEDILAK2", "COM"))
        self.label_2.setText(_translate("DEDILAK2", "SlaveID"))
