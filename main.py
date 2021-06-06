import sys
from Logic.LoginWidget import LoginWidget
from PySide6.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication([])
    login_window = LoginWidget()
    login_window.show()
    sys.exit(app.exec())

