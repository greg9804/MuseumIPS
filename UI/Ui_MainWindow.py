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
        MainWindow.resize(882, 566)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 861, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.searchTab = QWidget()
        self.searchTab.setObjectName(u"searchTab")
        self.gridLayoutWidget = QWidget(self.searchTab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 841, 471))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 9, 0, 1, 3)

        self.dateEdit_4 = QDateEdit(self.gridLayoutWidget)
        self.dateEdit_4.setObjectName(u"dateEdit_4")

        self.gridLayout.addWidget(self.dateEdit_4, 7, 2, 1, 1)

        self.checkBox_7 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout.addWidget(self.checkBox_7, 7, 1, 1, 1)

        self.checkBox_5 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout.addWidget(self.checkBox_5, 5, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.clearButton1 = QPushButton(self.gridLayoutWidget)
        self.clearButton1.setObjectName(u"clearButton1")

        self.gridLayout.addWidget(self.clearButton1, 8, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 2, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout.addWidget(self.checkBox_6, 6, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 4, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.findPushButton = QPushButton(self.gridLayoutWidget)
        self.findPushButton.setObjectName(u"findPushButton")

        self.gridLayout.addWidget(self.findPushButton, 8, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.dateEdit_3 = QDateEdit(self.gridLayoutWidget)
        self.dateEdit_3.setObjectName(u"dateEdit_3")

        self.gridLayout.addWidget(self.dateEdit_3, 6, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 3, 2, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 3, 1, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 2, 2, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(False)

        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 4, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 5, 2, 1, 1)

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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u041f\u0421 \u0443\u0447\u0435\u0442\u0430 \u043a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u0438 \u043c\u0443\u0437\u0435\u044f", None))
        self.checkBox_7.setText("")
        self.checkBox_5.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f (\u043e\u0442):", None))
        self.clearButton1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.checkBox_2.setText("")
        self.checkBox_6.setText("")
        self.checkBox_4.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f (\u043e\u0442):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f (\u0434\u043e):", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f (\u0434\u043e):", None))
        self.findPushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430, \u043e\u0434\u043d\u043e (\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439) \u0438\u043b\u0438 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e (\u0440\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435:", None))
        self.checkBox_3.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e", None))

        self.checkBox.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchTab), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diagrammaTab), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statTab), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.expoTab), QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442/\u0438\u043c\u043f\u043e\u0440\u0442 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editTab), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0411\u0414", None))
    # retranslateUi

