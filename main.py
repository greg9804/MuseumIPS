import sys

from login import Ui_LoginForm
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = QWidget()
    ui_login = Ui_LoginForm()
    ui_login.setupUi(login_form)
    login_form.show()
    sys.exit(app.exec_())

