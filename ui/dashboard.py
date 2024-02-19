# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 1126)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #ffffff;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 0, 121, 1081))
        self.frame.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 110, 77, 441))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("QFrame {\n"
"    border-radius: 23px;\n"
"    background-color: #fafafa; \n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton_Home = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_Home.setStyleSheet("QToolButton {\n"
"    border-radius: 19px; \n"
"    width: 50px; \n"
"    height: 50px; \n"
"    background-color: #fafafa; /* default background */\n"
"    text-align: center;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #d5fe63; /* background color for active state */\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_Home.setIcon(icon)
        self.toolButton_Home.setIconSize(QtCore.QSize(28, 28))
        self.toolButton_Home.setCheckable(True)
        self.toolButton_Home.setObjectName("toolButton_Home")
        self.verticalLayout.addWidget(self.toolButton_Home)
        self.toolButton_Members = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_Members.setStyleSheet("QToolButton {\n"
"    border-radius: 19px; \n"
"    width: 50px; \n"
"    height: 50px; \n"
"    background-color: #ffffff; /* default background */\n"
"    text-align: center;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #d5fe63; /* background color for active state */\n"
"}\n"
"")
        self.toolButton_Members.setCheckable(True)
        self.toolButton_Members.setObjectName("toolButton_Members")
        self.verticalLayout.addWidget(self.toolButton_Members)
        self.toolButton_Payment = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_Payment.setStyleSheet("QToolButton {\n"
"    border-radius: 19px; \n"
"    width: 50px; \n"
"    height: 50px; \n"
"    background-color: #ffffff; /* default background */\n"
"    text-align: center;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #d5fe63; /* background color for active state */\n"
"}\n"
"")
        self.toolButton_Payment.setCheckable(True)
        self.toolButton_Payment.setObjectName("toolButton_Payment")
        self.verticalLayout.addWidget(self.toolButton_Payment)
        self.toolButton_ = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_.setStyleSheet("QToolButton {\n"
"    border-radius: 19px; \n"
"    width: 50px; \n"
"    height: 50px; \n"
"    background-color: #ffffff; /* default background */\n"
"    text-align: center;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #d5fe63; /* background color for active state */\n"
"}\n"
"")
        self.toolButton_.setCheckable(True)
        self.toolButton_.setObjectName("toolButton_")
        self.verticalLayout.addWidget(self.toolButton_)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(20, 600, 77, 241))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet("QFrame {\n"
"    border-radius: 23px;\n"
"    background-color: #fafafa; \n"
"}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toolButton_Payment_2 = QtWidgets.QToolButton(self.frame_3)
        self.toolButton_Payment_2.setStyleSheet("QToolButton {\n"
"    border-radius: 19px; \n"
"    width: 50px; \n"
"    height: 50px; \n"
"    background-color: #ffffff; /* default background */\n"
"    text-align: center;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #d5fe63; /* background color for active state */\n"
"}\n"
"")
        self.toolButton_Payment_2.setCheckable(True)
        self.toolButton_Payment_2.setObjectName("toolButton_Payment_2")
        self.verticalLayout_2.addWidget(self.toolButton_Payment_2)
        self.toolButton_1 = QtWidgets.QToolButton(self.frame_3)
        self.toolButton_1.setStyleSheet("QToolButton {\n"
"    border-radius: 19px; \n"
"    width: 50px; \n"
"    height: 50px; \n"
"    background-color: #ffffff; /* default background */\n"
"    text-align: center;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #d5fe63; /* background color for active state */\n"
"}\n"
"")
        self.toolButton_1.setCheckable(True)
        self.toolButton_1.setObjectName("toolButton_1")
        self.verticalLayout_2.addWidget(self.toolButton_1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(120, 100, 1651, 71))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(160, 110, 261, 61))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet("QFrame {\n"
"    border-radius: 30px;\n"
"    background-color: #fafafa; \n"
"}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.frame_9.setStyleSheet("border-radius: 20px;\n"
"background-color: #f2f2f2;\n"
"")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(60, 10, 81, 16))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #9c9c9c;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 151, 16))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setItalic(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #4c4c4c;")
        self.label_2.setObjectName("label_2")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(1040, 110, 201, 61))
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setStyleSheet("QFrame {\n"
"    border-radius: 30px;\n"
"    background-color: #fafafa; \n"
"}\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.frame_10.setStyleSheet("border-radius: 20px;\n"
"background-color: #f2f2f2;\n"
"")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setGeometry(QtCore.QRect(70, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #9c9c9c;\n"
"")
        self.label_4.setObjectName("label_4")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(770, 110, 241, 61))
        self.frame_7.setAutoFillBackground(False)
        self.frame_7.setStyleSheet("QFrame {\n"
"    border-radius: 30px;\n"
"    background-color: #fafafa; \n"
"}\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.frame_8.setStyleSheet("border-radius: 20px;\n"
"background-color: #f2f2f2;\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setGeometry(QtCore.QRect(60, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #9c9c9c;\n"
"")
        self.label_3.setObjectName("label_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setGeometry(QtCore.QRect(160, 250, 441, 341))
        self.frame_11.setAutoFillBackground(False)
        self.frame_11.setStyleSheet("QFrame {\n"
"    border-radius: 30px;\n"
"    background-color: #fafafa; \n"
"}\n"
"")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.frame_12 = QtWidgets.QFrame(self.centralwidget)
        self.frame_12.setGeometry(QtCore.QRect(650, 250, 611, 341))
        self.frame_12.setAutoFillBackground(False)
        self.frame_12.setStyleSheet("QFrame {\n"
"    border-radius: 30px;\n"
"    background-color: #fafafa; \n"
"}\n"
"")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.frame_12.raise_()
        self.frame.raise_()
        self.frame_4.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.splitter.raise_()
        self.splitter_2.raise_()
        self.frame_11.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton_Home.setText(_translate("MainWindow", "..."))
        self.toolButton_Members.setText(_translate("MainWindow", "..."))
        self.toolButton_Payment.setText(_translate("MainWindow", "..."))
        self.toolButton_.setText(_translate("MainWindow", "..."))
        self.toolButton_Payment_2.setText(_translate("MainWindow", "..."))
        self.toolButton_1.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Hello Again!"))
        self.label_2.setText(_translate("MainWindow", "Tharuka Ravisara"))
        self.label_4.setText(_translate("MainWindow", "Notifications"))
        self.label_3.setText(_translate("MainWindow", "Search Members"))