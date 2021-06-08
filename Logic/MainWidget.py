import PySide6
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QDate

from Logic.Collection import Collection
from Logic.Search import Search
from UI.Ui_MainWindow import Ui_MainWindow


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.coll = Collection()
        self.coll.load()

        #НАСТРОЙКИ ПОИСКА
        for c in self.coll.getCountriesForCB():
            self.ui.comboBox.addItem(c)

        self.enableToggleSearchComponents()

        self.ui.findPushButton.clicked.connect(self.findExponat)
        self.ui.clearButton1.clicked.connect(self.clearInputs)

        #НАСТРОЙКИ ДИАГРАММЫ


    def enableToggleSearchComponents(self):
        # включение выключение компонентов поиска
        self.cb1 = self.ui.checkBox  # название
        self.cb2 = self.ui.checkBox_2  # место создания
        self.cb3 = self.ui.checkBox_3  # примечание
        self.cb4 = self.ui.checkBox_4  # год создания от
        self.cb5 = self.ui.checkBox_5  # год создания до
        self.cb6 = self.ui.checkBox_6  # дата поступления от
        self.cb7 = self.ui.checkBox_7  # дата поступления до

        self.ui.lineEdit.setDisabled(self.cb1.checkState() == QtCore.Qt.Unchecked)
        self.cb1.stateChanged.connect(lambda state: self.ui.lineEdit.setDisabled(state == QtCore.Qt.Unchecked))

        self.ui.comboBox.setDisabled(self.cb2.checkState() == QtCore.Qt.Unchecked)
        self.cb2.stateChanged.connect(lambda state: self.ui.comboBox.setDisabled(self.cb2.checkState() == QtCore.Qt.Unchecked))

        self.ui.lineEdit_2.setDisabled(self.cb3.checkState() == QtCore.Qt.Unchecked)
        self.cb3.stateChanged.connect(lambda state: self.ui.lineEdit_2.setDisabled(state == QtCore.Qt.Unchecked))

        self.ui.lineEdit_3.setDisabled(self.cb4.checkState() == QtCore.Qt.Unchecked)
        self.cb4.stateChanged.connect(lambda state: self.ui.lineEdit_3.setDisabled(self.cb4.checkState() == QtCore.Qt.Unchecked))

        self.ui.lineEdit_4.setDisabled(self.cb5.checkState() == QtCore.Qt.Unchecked)
        self.cb5.stateChanged.connect(lambda state: self.ui.lineEdit_4.setDisabled(self.cb5.checkState() == QtCore.Qt.Unchecked))

        self.ui.dateEdit_3.setDisabled(self.cb6.checkState() == QtCore.Qt.Unchecked)
        self.cb6.stateChanged.connect(lambda state: self.ui.dateEdit_3.setDisabled(self.cb6.checkState() == QtCore.Qt.Unchecked))

        self.ui.dateEdit_4.setDisabled(self.cb7.checkState() == QtCore.Qt.Unchecked)
        self.cb7.stateChanged.connect(lambda state: self.ui.dateEdit_4.setDisabled(self.cb7.checkState() == QtCore.Qt.Unchecked))
        ############################################


    def findExponat(self):
        params = {}
        if (self.cb1.checkState()):
            params["searchLine"] = self.ui.lineEdit.text()
        if (self.cb2.checkState()):
            params["cb"] = self.ui.comboBox.currentText()
        if (self.cb3.checkState()):
            params["note"] = self.ui.lineEdit_2.text()
        if (self.cb4.checkState()):
            params["yearbegin"] = self.ui.lineEdit_3.text()
        if (self.cb5.checkState()):
            params["yearend"] = self.ui.lineEdit_4.text()
        if (self.cb6.checkState()):
            params["datein_begin"] = self.ui.dateEdit_3.text()
        if (self.cb7.checkState()):
            params["datein_end"] = self.ui.dateEdit_4.text()
        searcher = Search(params, self.coll.Exponats)
        result = searcher.start()
        self.updateTableWidget(result)

    def updateTableWidget(self, lst):
        table = self.ui.tableWidget
        table.setRowCount(len(lst))
        row = 0
        for i in lst:
            print("!!!", i.name)
            table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i.id)))
            table.setItem(row, 1, QtWidgets.QTableWidgetItem(i.name))
            table.setItem(row, 2, QtWidgets.QTableWidgetItem(i.autor.fullname))
            table.setItem(row, 3, QtWidgets.QTableWidgetItem(i.type))
            table.setItem(row, 4, QtWidgets.QTableWidgetItem(i.style))
            table.setItem(row, 5, QtWidgets.QTableWidgetItem(str(i.year)))
            table.setItem(row, 6, QtWidgets.QTableWidgetItem(i.place))
            table.setItem(row, 7, QtWidgets.QTableWidgetItem(i.date_in.toString("yyyy-MM-dd")))
            table.setItem(row, 8, QtWidgets.QTableWidgetItem(i.admission))
            table.setItem(row, 9, QtWidgets.QTableWidgetItem(i.demo))
            table.setItem(row, 10, QtWidgets.QTableWidgetItem(i.note))
            row += 1

    def clearInputs(self):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.comboBox.setCurrentIndex(0)
        date = QDate()
        self.ui.dateEdit_3.setDate(date.currentDate())
        self.ui.dateEdit_4.setDate(date.currentDate())
        self.cb1.setChecked(False)
        self.cb2.setChecked(False)
        self.cb3.setChecked(False)
        self.cb4.setChecked(False)
        self.cb5.setChecked(False)
        self.cb6.setChecked(False)
        self.cb7.setChecked(False)
