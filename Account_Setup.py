# Form implementation generated from reading ui file 'Account_Setup.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SetupWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_login = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(110, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.label_username = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(20, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(20, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.input_username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_username.setGeometry(QtCore.QRect(120, 140, 113, 21))
        self.input_username.setObjectName("input_username")
        self.input_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_password.setGeometry(QtCore.QRect(120, 180, 113, 20))
        self.input_password.setObjectName("input_password")
        self.button_login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(20, 230, 101, 41))
        self.button_login.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")
        self.button_create = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_create.setGeometry(QtCore.QRect(140, 230, 101, 41))
        self.button_create.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_create.setFont(font)
        self.button_create.setObjectName("button_create")
        self.label_error = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(30, 300, 211, 21))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bank_Login"))
        self.label_title.setText(_translate("MainWindow", "Bank Of Nebraska "))
        self.label_login.setText(_translate("MainWindow", "Login"))
        self.label_username.setText(_translate("MainWindow", "UserName:"))
        self.label_password.setText(_translate("MainWindow", "Password:"))
        self.button_login.setText(_translate("MainWindow", "LOGIN"))
        self.button_create.setText(_translate("MainWindow", "CREATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SetupWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
