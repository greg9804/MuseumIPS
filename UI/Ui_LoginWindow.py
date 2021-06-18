# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(423, 304)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(14)
        LoginWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"UI/iconn.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet(u"QPushButton {\n"
"	padding: 5px;\n"
"	font: 14pt \"Tahoma\";\n"
"    border: 2px solid rgb(170, 13, 47);\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 13, 47);\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"	color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.gridLayoutWidget = QWidget(LoginWindow)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 411, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.userLoginBtn = QPushButton(self.gridLayoutWidget)
        self.userLoginBtn.setObjectName(u"userLoginBtn")

        self.gridLayout.addWidget(self.userLoginBtn, 1, 0, 1, 1)

        self.workerLoginBtn = QPushButton(self.gridLayoutWidget)
        self.workerLoginBtn.setObjectName(u"workerLoginBtn")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.workerLoginBtn.setFont(font1)

        self.gridLayout.addWidget(self.workerLoginBtn, 1, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {\n"
"	color: rgb(32, 12, 255);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(0)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.userLoginBtn.setText(QCoreApplication.translate("LoginWindow", u"\u041a\u0430\u043a \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.workerLoginBtn.setText(QCoreApplication.translate("LoginWindow", u"\u041a\u0430\u043a \u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a \u043c\u0443\u0437\u0435\u044f", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c!</span></p><p align=\"center\"><span style=\" font-size:14pt;\">\u041a\u0430\u043a \u0432\u043e\u0439\u0442\u0438 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443?</span></p></body></html>", None))
    # retranslateUi

