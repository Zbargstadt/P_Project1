# Form implementation generated from reading ui file 'Account_Bank.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Account_Bank(object):
    def setupUi(self, Account_Bank):
        Account_Bank.setObjectName("Account_Bank")
        Account_Bank.resize(400, 400)
        Account_Bank.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(parent=Account_Bank)
        self.centralwidget.setObjectName("centralwidget")
        self.label_bank = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_bank.setGeometry(QtCore.QRect(110, 0, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_bank.setFont(font)
        self.label_bank.setObjectName("label_bank")
        self.label_account_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_account_name.setGeometry(QtCore.QRect(20, 80, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        font.setUnderline(False)
        self.label_account_name.setFont(font)
        self.label_account_name.setObjectName("label_account_name")
        self.label_balance = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_balance.setGeometry(QtCore.QRect(50, 150, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_balance.setFont(font)
        self.label_balance.setObjectName("label_balance")
        self.button_deposit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_deposit.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.button_deposit.setObjectName("button_deposit")
        self.button_withdraw = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_withdraw.setGeometry(QtCore.QRect(210, 230, 75, 23))
        self.button_withdraw.setObjectName("button_withdraw")
        self.input_amount = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(80, 190, 201, 20))
        self.input_amount.setObjectName("input_amount")
        self.label_account_type = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_account_type.setGeometry(QtCore.QRect(20, 50, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_account_type.setFont(font)
        self.label_account_type.setObjectName("label_account_type")
        self.label_validity = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_validity.setGeometry(QtCore.QRect(150, 270, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_validity.setFont(font)
        self.label_validity.setText("")
        self.label_validity.setObjectName("label_validity")
        self.label_errors = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_errors.setGeometry(QtCore.QRect(80, 300, 241, 16))
        self.label_errors.setText("")
        self.label_errors.setObjectName("label_errors")
        Account_Bank.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Account_Bank)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        Account_Bank.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Account_Bank)
        self.statusbar.setObjectName("statusbar")
        Account_Bank.setStatusBar(self.statusbar)

        self.retranslateUi(Account_Bank)
        QtCore.QMetaObject.connectSlotsByName(Account_Bank)

    def retranslateUi(self, Account_Bank):
        _translate = QtCore.QCoreApplication.translate
        Account_Bank.setWindowTitle(_translate("Account_Bank", "Account_Bank"))
        self.label_bank.setText(_translate("Account_Bank", "Bank Of Nebraska "))
        self.label_account_name.setText(_translate("Account_Bank", "Welcome Account Name"))
        self.label_balance.setText(_translate("Account_Bank", "Balance: "))
        self.button_deposit.setText(_translate("Account_Bank", "Deposit"))
        self.button_withdraw.setText(_translate("Account_Bank", "Withdraw"))
        self.label_account_type.setText(_translate("Account_Bank", "Checking Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account_Bank = QtWidgets.QMainWindow()
    ui = Ui_Account_Bank()
    ui.setupUi(Account_Bank)
    Account_Bank.show()
    sys.exit(app.exec())