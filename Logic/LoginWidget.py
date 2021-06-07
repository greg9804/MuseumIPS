from Logic.MainWidget import MainWidget
from UI.Ui_LoginWindow import Ui_LoginWindow
from PySide6 import QtWidgets


class LoginWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.userLoginBtn.clicked.connect(self.show_main_window)
        self.ui.workerLoginBtn.clicked.connect(self.auth_worker)

    def show_main_window(self):
        self.hide()
        #QtWidgets.QMessageBox.information(self, "Вход в систему", "Здравствуйте, вход выполнен!", buttons=QtWidgets.QMessageBox.Ok)
        self.main_window = MainWidget()
        self.main_window.show()

    def auth_worker(self):
        key,ok = QtWidgets.QInputDialog.getText(self, "Вход в систему", "Введите ваш ключ")

        if ok and key == "123":
            self.show_main_window()


