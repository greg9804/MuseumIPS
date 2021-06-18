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
        MainWindow.resize(943, 582)
        icon = QIcon()
        icon.addFile(u"UI/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background: rgb(255, 244, 201);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 921, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid rgb(65, 65, 64);\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.130682 rgba(120, 54, 50, 255), stop:0.715909 rgba(138, 70, 97, 255), stop:1 rgba(0, 70, 235, 255));\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 10px;\n"
"	color: rgb(98, 174, 107);\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop:"
                        " 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgb(9, 69, 121); \n"
"	font: 12pt \"Tahoma\";\n"
"}\n"
"\n"
"QPushButton {\n"
"	\n"
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
"    border-color: navy; /* mak"
                        "e the default button prominent */\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid  rgb(0, 255, 255);\n"
"    border-radius: 1px;\n"
"    padding: 5px 15px 5px 3px;\n"
"    min-width: 6em;\n"
"	font: 12pt \"Tahoma\";\n"
"	color: rgb(56, 112, 0);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    "
                        "padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.searchTab = QWidget()
        self.searchTab.setObjectName(u"searchTab")
        self.gridLayoutWidget = QWidget(self.searchTab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 901, 471))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 4, 2, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(False)

        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 4, 1, 1, 1)

        self.findPushButton = QPushButton(self.gridLayoutWidget)
        self.findPushButton.setObjectName(u"findPushButton")

        self.gridLayout.addWidget(self.findPushButton, 8, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 3, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.clearButton1 = QPushButton(self.gridLayoutWidget)
        self.clearButton1.setObjectName(u"clearButton1")

        self.gridLayout.addWidget(self.clearButton1, 8, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout.addWidget(self.checkBox_5, 5, 1, 1, 1)

        self.checkBox_7 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout.addWidget(self.checkBox_7, 7, 1, 1, 1)

        self.dateEdit_3 = QDateEdit(self.gridLayoutWidget)
        self.dateEdit_3.setObjectName(u"dateEdit_3")

        self.gridLayout.addWidget(self.dateEdit_3, 6, 2, 1, 1)

        self.dateEdit_4 = QDateEdit(self.gridLayoutWidget)
        self.dateEdit_4.setObjectName(u"dateEdit_4")

        self.gridLayout.addWidget(self.dateEdit_4, 7, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 2, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 2, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 5, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout.addWidget(self.checkBox_6, 6, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 3, 1, 1, 1)

        self.tableWidget = QTableWidget(self.gridLayoutWidget)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 9, 0, 1, 3)

        self.tabWidget.addTab(self.searchTab, "")
        self.diagrammTab = QWidget()
        self.diagrammTab.setObjectName(u"diagrammTab")
        self.verticalLayoutWidget_2 = QWidget(self.diagrammTab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 50, 891, 441))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButtonDiag = QPushButton(self.diagrammTab)
        self.pushButtonDiag.setObjectName(u"pushButtonDiag")
        self.pushButtonDiag.setGeometry(QRect(10, 10, 891, 31))
        self.tabWidget.addTab(self.diagrammTab, "")
        self.statTab = QWidget()
        self.statTab.setObjectName(u"statTab")
        self.gridLayoutWidget_2 = QWidget(self.statTab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 10, 911, 491))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_2 = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_2.addWidget(self.radioButton_2, 3, 0, 1, 1)

        self.radioButton_4 = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_2.addWidget(self.radioButton_4, 5, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_2.addWidget(self.radioButton_3, 4, 0, 1, 1)

        self.radioButton_6 = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout_2.addWidget(self.radioButton_6, 7, 0, 1, 1)

        self.radioButton_5 = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_2.addWidget(self.radioButton_5, 6, 0, 1, 1)

        self.pushButtonStat = QPushButton(self.gridLayoutWidget_2)
        self.pushButtonStat.setObjectName(u"pushButtonStat")

        self.gridLayout_2.addWidget(self.pushButtonStat, 1, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_2.addWidget(self.radioButton, 2, 0, 1, 1)

        self.listWidget = QListWidget(self.gridLayoutWidget_2)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_2.addWidget(self.listWidget, 8, 0, 1, 1)

        self.tabWidget.addTab(self.statTab, "")
        self.expoTab = QWidget()
        self.expoTab.setObjectName(u"expoTab")
        self.gridLayoutWidget_3 = QWidget(self.expoTab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 908, 481))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_3.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.pushButtonClr2 = QPushButton(self.gridLayoutWidget_3)
        self.pushButtonClr2.setObjectName(u"pushButtonClr2")

        self.gridLayout_3.addWidget(self.pushButtonClr2, 1, 1, 1, 1)

        self.pushButtonExport = QPushButton(self.gridLayoutWidget_3)
        self.pushButtonExport.setObjectName(u"pushButtonExport")

        self.gridLayout_3.addWidget(self.pushButtonExport, 1, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)

        self.pushButtonImport = QPushButton(self.gridLayoutWidget_3)
        self.pushButtonImport.setObjectName(u"pushButtonImport")

        self.gridLayout_3.addWidget(self.pushButtonImport, 2, 1, 1, 1)

        self.tabWidget.addTab(self.expoTab, "")
        self.editTab = QWidget()
        self.editTab.setObjectName(u"editTab")
        self.pushButtonEdit = QPushButton(self.editTab)
        self.pushButtonEdit.setObjectName(u"pushButtonEdit")
        self.pushButtonEdit.setGeometry(QRect(320, 200, 271, 81))
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
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f (\u0434\u043e):", None))
        self.checkBox.setText("")
        self.checkBox_4.setText("")
        self.findPushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430, \u043e\u0434\u043d\u043e (\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439) \u0438\u043b\u0438 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e (\u0440\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a):", None))
        self.clearButton1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f (\u043e\u0442):", None))
        self.checkBox_5.setText("")
        self.checkBox_7.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e", None))

        self.checkBox_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f (\u0434\u043e):", None))
        self.checkBox_6.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f (\u043e\u0442):", None))
        self.checkBox_3.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0430\u0432\u0442\u043e\u0440\u0430", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0438\u043b\u044c", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a \u043f\u043e\u043f\u0430\u043b", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchTab), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u043e\u0432", None))
        self.pushButtonDiag.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diagrammTab), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0442\u0438\u043f\u0443", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0433\u043e\u0434\u0443 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0441\u0442\u0438\u043b\u044e", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043c\u0435\u0441\u0442\u0443 \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u0438/\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0441\u043f\u043e\u0441\u043e\u0431\u0443 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0432 \u043c\u0443\u0437\u0435\u0439", None))
        self.pushButtonStat.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u0441\u044e \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0443 \u0432 \u0444\u0430\u0439\u043b", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u043e\u0432 \u043f\u043e \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u043c \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u044f\u043c", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u043f\u043e \u0430\u0432\u0442\u043e\u0440\u0430\u043c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statTab), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 id \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u043e\u0432 \u0434\u043b\u044f \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430 \u043f\u043e \u043e\u0434\u043d\u043e\u043c\u0443,\n"
"\u0447\u0435\u0440\u0435\u0437 \u0437\u0430\u043f\u044f\u0442\u0443\u044e \u0438\u043b\u0438 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0447\u0435\u0440\u0435\u0437 \u0434\u0435\u0444\u0438\u0441:", None))
        self.pushButtonClr2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441 \u043f\u043e\u043b\u044f", None))
        self.pushButtonExport.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0434\u043b\u044f \u0438\u043c\u043f\u043e\u0440\u0442\u0430 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u043e\u0432:", None))
        self.pushButtonImport.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b \u0438 \u0438\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.expoTab), QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442/\u0438\u043c\u043f\u043e\u0440\u0442 \u044d\u043a\u0441\u043f\u043e\u043d\u0430\u0442\u043e\u0432", None))
        self.pushButtonEdit.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043e\u043a\u043d\u043e \u0440\u0435\u0434\u0430\u043a\u0442\u043e\u0440\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editTab), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0411\u0414", None))
    # retranslateUi

