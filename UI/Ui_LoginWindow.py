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
        LoginWindow.resize(400, 300)
        self.gridLayoutWidget = QWidget(LoginWindow)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 381, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.userLoginBtn = QPushButton(self.gridLayoutWidget)
        self.userLoginBtn.setObjectName(u"userLoginBtn")

        self.gridLayout.addWidget(self.userLoginBtn, 1, 0, 1, 1)

        self.workerLoginBtn = QPushButton(self.gridLayoutWidget)
        self.workerLoginBtn.setObjectName(u"workerLoginBtn")

        self.gridLayout.addWidget(self.workerLoginBtn, 1, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
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

