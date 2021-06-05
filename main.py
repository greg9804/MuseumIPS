import sys

from UI.login import UiLoginForm
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)

    sys.exit(app.exec_())

