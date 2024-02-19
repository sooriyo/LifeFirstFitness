import sys
from PyQt5.QtWidgets import QApplication
from controllers.login_controller import LoginController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = LoginController()
    sys.exit(app.exec_())
