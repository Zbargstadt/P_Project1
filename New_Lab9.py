from PyQt6.QtWidgets import *
from Account_Setup import *
from Account_Bank import *
import csv, os.path


class Logic_Setup(QMainWindow, Ui_SetupWindow):
    '''
    Class that applies the Login GUI
    Also houses functions login and create
    '''
    def __init__(self) -> None:
        '''
        Initializes Login Gui
        '''
        super().__init__()
        self.setupUi(self)
        self.button_login.clicked.connect(lambda: self.login())
        self.button_create.clicked.connect(lambda: self.create())

    def login(self) -> None:
        '''
        Allows user to login into saved account
        :return: Access Bank GUI
        '''
        Logic_Setup.login_list = [self.input_username.text(), self.input_password.text()]
        if os.path.isfile(f'files\\names.csv'):
            with open('files\\names.csv', 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if self.input_username.text() == line[0]:
                        if self.input_password.text() == line[1]:
                            self.application = QApplication([])
                            self.window = Logic_Bank()
                            self.window.show()
                            self.application.exec()
                        else:
                            self.label_error.setText('ERROR: Incorrect Password')
                            break
                    else:
                        self.label_error.setText('ERROR: User Doesnt Exist')
        else:
            self.label_error.setText('ERROR: No Users Yet')
    def create(self) -> None:
        '''
        Allows user to create new account
        :return: Access Bank GUI
        '''
        Logic_Setup.login_list = [self.input_username.text(), self.input_password.text()]
        repeat = False
        if os.path.isfile(f'files\\names.csv'):
            with open('files\\names.csv', 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if self.input_username.text() == line[0]:
                        self.label_error.setText('ERROR: User Already Exists')
                        repeat = True
                if repeat is False:
                    with open('files\\names.csv', 'a', newline='') as c_file:
                        csv_writer = csv.writer(c_file)
                        csv_writer.writerow(Logic_Setup.login_list)
                    self.application = QApplication([])
                    self.window = Logic_Bank()
                    self.window.show()
                    self.application.exec()

        else:
            with open('files\\names.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                header = ['Username', 'Password']
                csv_writer.writerow(header)
                csv_writer.writerow(Logic_Setup.login_list)
            self.application = QApplication([])
            self.window = Logic_Bank()
            self.window.show()
            self.application.exec()


class Logic_Bank(QMainWindow, Ui_Account_Bank):
    '''
    Class that applies the Bank GUI
    Also houses functions deposit and withdraw
    '''
    def __init__(self) -> None:
        '''
        Initializes GUI
        '''
        super().__init__()
        self.setupUi(self)
        Logic_Setup.account_balance = 0
        self.label_account_name.setText(f'Welcome {Logic_Setup.login_list[0]}')
        if os.path.isfile(f'files\\{Logic_Setup.login_list[0]}.csv'):
            with open(f'files\\{Logic_Setup.login_list[0]}.csv', 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for line in csv_reader:
                    Logic_Setup.account_balance = line[0]
        self.label_balance.setText(f'Balance: {Logic_Setup.account_balance}')
        self.button_deposit.clicked.connect(lambda: self.deposit())
        self.button_withdraw.clicked.connect(lambda: self.withdraw())

    def deposit(self) -> None:
        '''
        Allows user to deposit money into balance
        :return:
        '''
        self.label_errors.setText('')
        try:
            amount = float(self.input_amount.text())
            Logic_Setup.account_balance = Logic_Setup.account_balance + amount
            self.label_validity.setText('Valid Deposit')
            self.label_balance.setText(f'Balance: {Logic_Setup.account_balance}')
            with open(f'files\\{Logic_Setup.login_list[0]}.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                header = ['Balance']
                csv_writer.writerow(header)
                balance = [Logic_Setup.account_balance]
                csv_writer.writerow(balance)
        except:
            self.label_validity.setText('Invalid Deposit')
            self.label_errors.setText('Error: Must be a positive number')

    def withdraw(self) -> None:
        '''
        Allows user to withdraw money from balance
        :return:
        '''
        self.label_errors.setText('')
        try:
            amount = float(self.input_amount.text())
            Logic_Setup.account_balance = Logic_Setup.account_balance - amount
            if Logic_Setup.account_balance < 0:
                self.label_validity.setText('Invalid Withdraw')
                self.label_errors.setText('Error: Negative Balance')
                Logic_Setup.account_balance = Logic_Setup.account_balance + amount
            else:
                self.label_validity.setText('Valid Withdraw')
                self.label_balance.setText(f'Balance: {Logic_Setup.account_balance}')
            with open(f'files\\{Logic_Setup.login_list[0]}.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                header = ['Balance']
                csv_writer.writerow(header)
                balance = [Logic_Setup.account_balance]
                csv_writer.writerow(balance)
        except:
            self.label_validity.setText('Invalid Withdraw')
            self.label_errors.setText('Error: Must be a positive number')