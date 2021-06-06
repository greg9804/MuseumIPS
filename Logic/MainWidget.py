from PySide6 import QtWidgets

from Logic.Collection import Collection
from UI.Ui_MainWindow import Ui_MainWindow


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        coll = Collection()
        coll.load()
