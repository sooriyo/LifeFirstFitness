from PyQt5.QtWidgets import QMainWindow, QButtonGroup, QToolButton
from views.dashboard_ui import Ui_MainWindow


class DashboardWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Create a button group for the tool buttons
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.setExclusive(True)

        # Add buttons to the group
        # Assuming you have toolButton_Home, toolButton_Members, etc., as names in your UI
        self.buttonGroup.addButton(self.toolButton_Home)
        self.buttonGroup.addButton(self.toolButton_Members)
        self.buttonGroup.addButton(self.toolButton_Payment)
        # Add all other tool buttons you want to include in the group

        # Connect the button clicked signal
        self.buttonGroup.buttonClicked.connect(self.updateButtonStyles)

        # Initial update of button styles
        self.updateButtonStyles()

    def updateButtonStyles(self):
        # Update the style for each button in the group
        for button in self.buttonGroup.buttons():
            if button.isChecked():
                button.setStyleSheet("QToolButton {"
                                     "border-radius: 19px;"
                                     "width: 50px;"
                                     "height: 50px;"
                                     "background-color: #d5fe63; }")  # Active state
            else:
                button.setStyleSheet("QToolButton {"
                                     "border-radius: 19px;"
                                     "width: 50px;"
                                     "height: 50px;"
                                     "background-color: #ffffff; }")  # Inactive state
