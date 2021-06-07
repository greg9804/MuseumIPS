import PySide6
from PySide6 import QtWidgets
from PySide6.QtCore import QDate

from Logic.Collection import Collection
from Logic.Search import Search
from UI.Ui_MainWindow import Ui_MainWindow


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        coll = Collection()
        coll.load()

        countriesCB = coll.getCountriesForCB()
        for c in countriesCB:
            self.ui.comboBox.addItem(c)

        self.ui.findPushButton.clicked.connect(self.findExponat)
        self.ui.clearButton1.clicked.connect(self.clearInputs)

    def findExponat(self):
        params = {}
        params["searchLine"] = self.ui.lineEdit.text()
        params["cb"] = self.ui.comboBox.currentText()
        params["note"] = self.ui.lineEdit_2.text()
        params["yearbegin"] = self.ui.dateEdit.text()
        params["yearend"] = self.ui.dateEdit_2.text()
        params["datein_begin"] = self.ui.dateEdit_3.text()
        params["datein_end"] = self.ui.dateEdit_4.text()
        searcher = Search(params)
        searcher.start()

    def clearInputs(self):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.comboBox.setCurrentIndex(0)
        date = QDate()
        self.ui.dateEdit.setDate(date.currentDate())
        self.ui.dateEdit_2.setDate(date.currentDate())
        self.ui.dateEdit_3.setDate(date.currentDate())
        self.ui.dateEdit_4.setDate(date.currentDate())