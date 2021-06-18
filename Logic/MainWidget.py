import sys

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QDate, QRegularExpression
from PySide6.QtWidgets import QButtonGroup, QFileDialog

from Logic.Collection import Collection
from Logic.Diagramm import Diagramm
from Logic.EditWindow import EditWindow
from Logic.Search import Search
from Logic.Statistics import Statistics
from Logic.WorkExpo import WorkExpo
from UI.Ui_MainWindow import Ui_MainWindow


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self, withKey=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.coll = Collection()
        self.coll.load()
        self.withKey = withKey

        if not self.withKey:
            self.ui.expoTab.setDisabled(True)
            self.ui.editTab.setDisabled(True)

        #НАСТРОЙКИ ПОИСКА
        for c in self.coll.getCountriesForCB():
            self.ui.comboBox.addItem(c)

        self.enableToggleSearchComponents()
        self.setupValidators()

        self.ui.findPushButton.clicked.connect(self.findExponat)
        self.ui.clearButton1.clicked.connect(self.clearInputs)

        #НАСТРОЙКИ ДИАГРАММЫ
        self.ui.pushButtonDiag.clicked.connect(self.createDiagramm)

        #НАСТРОЙКИ СТАТИСТИКИ
        self.ui.tabWidget.currentChanged.connect(self.whichTabIsSelected)

        #НАСТРОЙКИ ЭКСПОРТА/ИМПОРТА
        self.ui.pushButtonClr2.clicked.connect(self.clr2)
        self.ui.pushButtonExport.clicked.connect(self.startExport)
        self.ui.pushButtonImport.clicked.connect(self.startImport)

        #НАСТРОЙКИ РЕДАКТИРОВАНИЯ БД
        self.ui.pushButtonEdit.clicked.connect(self.startEdit)

    def reloadCollection(self):
        print('reloading...')
        self.coll.load()

    def startEdit(self):
        self.edit_window = EditWindow(self)
        self.edit_window.show()

    def startImport(self):
        worker = WorkExpo(self, self.coll)
        count = worker.import_from_file()
        if count > 0:
            self.coll.load()


    def startExport(self):
        ids = self.ui.lineEdit_5.text()
        if (ids == ""):
            QtWidgets.QMessageBox.warning(self, "Некорректный ввод данных", "Вы не ввели id экспонатов!",
                                          buttons=QtWidgets.QMessageBox.Cancel)
            return
        worker = WorkExpo(self, self.coll)
        if ids.find(",") != -1:
            ids = ids.split(",")
            worker.export(ids, 1)
        elif ids.find("-") != -1:
            ids = ids.split("-")
            worker.export(ids, 2)
        else:
            worker.export(ids, 3)
        self.clr2()

    def clr2(self):
        self.ui.lineEdit_5.setText("")

    def whichTabIsSelected(self):
        current_index = self.ui.tabWidget.currentIndex()
        print(current_index, "is curindex")
        if current_index == 2:
            self.createStatistics()


    def createStatistics(self):
        self.radios = QButtonGroup()
        self.radios.addButton(self.ui.radioButton)
        self.radios.addButton(self.ui.radioButton_2)
        self.radios.addButton(self.ui.radioButton_3)
        self.radios.addButton(self.ui.radioButton_4)
        self.radios.addButton(self.ui.radioButton_5)
        self.radios.addButton(self.ui.radioButton_6)
        self.radios.buttonClicked.connect(self.buildByGroup)
        self.ui.pushButtonStat.clicked.connect(self.buildToFile)


    def buildByGroup(self):
        id_radio = self.radios.checkedId()
        s = Statistics(self.coll)
        result = s.build(id_radio)
        self.ui.listWidget.clear()
        for r in result:
            self.ui.listWidget.addItem("%s : %d" % (r[0], r[1]))

    def buildToFile(self):
        filename, ok = QFileDialog.getSaveFileName(self,
                                                   "Сохранить файл",
                                                   ".",
                                                   "All Files(*.*)")
        print(filename, "!", ok)
        default_out = sys.stdout
        outfile = open(filename, 'w')
        sys.stdout = outfile

        s = Statistics(self.coll)
        result = s.buildToFile()
        for r in result:
            print("%s : %d" % (r[0], r[1]))

        sys.stdout = default_out
        outfile.close()

    def createDiagramm(self):
        d = Diagramm(self, self.ui.verticalLayout_2, self.coll)
        d.render()


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
        #для экспорта экспонатов
        rex_ex_lineEdit5 = QRegularExpression("^([0-9]{1,4})|(([0-9]{1,4},)+)|([0-9]{1,4}-[0-9]{1,4})$")
        lineEdit_validator = QtGui.QRegularExpressionValidator(reg_ex_lineEdit, self.ui.lineEdit)
        lineEdit2_validator = QtGui.QRegularExpressionValidator(reg_ex_lineEdit2, self.ui.lineEdit_2)
        lineEdit3_validator = QtGui.QRegularExpressionValidator(reg_ex_lineEdit3, self.ui.lineEdit_3)
        lineEdit4_validator = QtGui.QRegularExpressionValidator(reg_ex_lineEdit3, self.ui.lineEdit_4)
        lineEdit5_validator = QtGui.QRegularExpressionValidator(rex_ex_lineEdit5, self.ui.lineEdit_5)
        self.ui.lineEdit.setValidator(lineEdit_validator)
        self.ui.lineEdit_2.setValidator(lineEdit2_validator)
        self.ui.lineEdit_3.setValidator(lineEdit3_validator)
        self.ui.lineEdit_4.setValidator(lineEdit4_validator)
        self.ui.lineEdit_5.setValidator(lineEdit5_validator)

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
