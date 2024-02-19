from PyQt5.QtWidgets import QMessageBox, QWidget
from models.admin import Admin
from sqlalchemy.orm import Session
from database import SessionLocal
import bcrypt

from views.dashboard_window import DashboardWindow
from views.login_ui import Ui_Form


class LoginController(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.dashboard = None
        self.setupUi(self)
        self.loginButton.clicked.connect(self.check_credentials)
        self.show()

    def check_credentials(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text().encode('utf-8')  # Ensure password is in bytes for bcrypt

        db = SessionLocal()
        admin = db.query(Admin).filter(Admin.username == username).first()
        db.close()

        # Check if the admin exists and the password is correct
        if admin and self.verify_password(admin.hashed_password, password):
            self.open_dashboard()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    @staticmethod
    def verify_password(stored_password, provided_password):
        stored_password_bytes = stored_password if isinstance(stored_password, bytes) else stored_password.encode(
            'utf-8')
        return bcrypt.checkpw(provided_password, stored_password_bytes)

    def open_dashboard(self):
        self.dashboard = DashboardWindow()
        self.dashboard.show()
        self.close()
