import PySide6
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QDate, QRegularExpression
from PySide6.QtGui import QValidator

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
        self.setupValidators()

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

    def setupValidators(self):
        reg_ex_lineEdit = QRegularExpression("^[а-яА-Яa-zA-Z ]+$")
        reg_ex_lineEdit2 = QRegularExpression("^[а-яА-Яa-zA-Z0-9 ]+$")
        reg_ex_lineEdit3 = QRegularExpression("^[0-9]{4}")
        lineEdit_validator = QtGui.QRegularExpressionValidator(reg_ex_lineEdit, self.ui.lineEdit)
        lineEdit2_validator = QtGui.QRegularExpressionValidator(reg_ex_lineEdit2, self.ui.lineEdit_2)
        lineEdit3_validator = QtGui.QRegularExpressionValidator(reg_ex_lineEdit3, self.ui.lineEdit_3)
        lineEdit4_validator = QtGui.QRegularExpressionValidator(reg_ex_lineEdit3, self.ui.lineEdit_4)
        self.ui.lineEdit.setValidator(lineEdit_validator)
        self.ui.lineEdit_2.setValidator(lineEdit2_validator)
        self.ui.lineEdit_3.setValidator(lineEdit3_validator)
        self.ui.lineEdit_4.setValidator(lineEdit4_validator)

    def findExponat(self):
        params = {}
        c = 0
        if self.cb1.checkState():
            if self.ui.lineEdit.text() != "":
                params["searchLine"] = self.ui.lineEdit.text()
                c += 1
            else:
                QtWidgets.QMessageBox.warning(self, "Некорректный ввод данных", "Вы ввели пустую строку!", buttons=QtWidgets.QMessageBox.Cancel)
                self.clearInputs()
                return
        if self.cb2.checkState():
            if self.ui.comboBox.currentText() == "Не указано":
                QtWidgets.QMessageBox.warning(self, "Некорректный ввод данных", "Укажите местоположение!", buttons=QtWidgets.QMessageBox.Cancel)
                self.clearInputs()
                return
            else:
                params["cb"] = self.ui.comboBox.currentText()
                c += 1
        if self.cb3.checkState():
            if self.ui.lineEdit_2.text() != "":
                params["note"] = self.ui.lineEdit_2.text()
                c += 1
            else:
                QtWidgets.QMessageBox.warning(self, "Некорректный ввод данных", "Вы ввели пустую строку!", buttons=QtWidgets.QMessageBox.Cancel)
                self.clearInputs()
                return
        if self.cb4.checkState():
            if self.ui.lineEdit_3.text() != "":
                params["yearbegin"] = self.ui.lineEdit_3.text()
                c += 1
            else:
                QtWidgets.QMessageBox.warning(self, "Некорректный ввод данных", "Вы ввели пустую строку!", buttons=QtWidgets.QMessageBox.Cancel)
                self.clearInputs()
                return
        if self.cb5.checkState():
            if self.ui.lineEdit_4.text() != "":
                params["yearend"] = self.ui.lineEdit_4.text()
                c += 1
            else:
                QtWidgets.QMessageBox.warning(self, "Некорректный ввод данных", "Вы ввели пустую строку!", buttons=QtWidgets.QMessageBox.Cancel)
                self.clearInputs()
                return
        if self.cb6.checkState():
            params["datein_begin"] = self.ui.dateEdit_3.text()
            c += 1
        if self.cb7.checkState():
            params["datein_end"] = self.ui.dateEdit_4.text()
            c += 1
        if c != 0:
            searcher = Search(params, self.coll.Exponats)
            result = searcher.start()
            self.updateTableWidget(result)
        elif c == 0:
            QtWidgets.QMessageBox.warning(self, "Некорректный ввод данных", "Нет данных для поиска!", buttons=QtWidgets.QMessageBox.Cancel)
            self.clearInputs()
            return

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
