# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(921, 465)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 901, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.searchTab = QWidget()
        self.searchTab.setObjectName(u"searchTab")
        self.tabWidget.addTab(self.searchTab, "")
        self.diagrammaTab = QWidget()
        self.diagrammaTab.setObjectName(u"diagrammaTab")
        self.tabWidget.addTab(self.diagrammaTab, "")
        self.statTab = QWidget()
        self.statTab.setObjectName(u"statTab")
        self.tabWidget.addTab(self.statTab, "")
        self.expoTab = QWidget()
        self.expoTab.setObjectName(u"expoTab")
        self.tabWidget.addTab(self.expoTab, "")
        self.editTab = QWidget()
        self.editTab.setObjectName(u"editTab")
        self.tabWidget.addTab(self.editTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u041f\u0421 \u0443\u0447\u0435\u0442\u0430 \u043a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u0438 \u043c\u0443\u0437\u0435\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchTab), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diagrammaTab), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statTab), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.expoTab), QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442/\u0438\u043c\u043f\u043e\u0440\u0442 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editTab), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0411\u0414", None))
    # retranslateUi

