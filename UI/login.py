from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from packages.model import hospital
from PyQt5.QtCore import pyqtSlot

class login(QMainWindow):

    def __init__(self):
        super(login, self).__init__()
        self.usercode = ""
        self.password = ""

    def login_page_logic(self, change):
        login_button = change.main_window.findChild(QPushButton, "LoginPageLoginButton")
        login_button.clicked.connect(lambda: self.send_data_to_database(change, "LoginPage"))

        register_button = change.main_window.findChild(QPushButton, "LoginPageRegisterButton")
        register_button.clicked.connect(lambda: change.change_page(change, 2))

        forget_button = change.main_window.findChild(QPushButton, "LoginPageForgetButton")
        forget_button.clicked.connect(lambda: change.change_page(change, 3))

    @pyqtSlot()
    def send_data_to_database(self, change, string):
        print("Sending Data")
        login_text_edit = change.main_window.findChild(QLineEdit, "LoginPageUsernameLineEdit")
        password_text_edit = change.main_window.findChild(QLineEdit, "LoginPagePasswordLineEdit")
        change.usercode = self.get_data(login_text_edit)
        change.password = self.get_data(password_text_edit)

        if self.usercode != 0 and self.password != 0:
            self.check_authentication(change)

    def get_data(self, item):
        if item.text() == "" and "Field" not in item.placeholderText():
            text = item.placeholderText()
            item.setPlaceholderText("Fill Field: " + text)
            item.setStyleSheet("QLineEdit{ "
                               "border:none;"
                               "border-radius:5;"
                               "background-color:#af2b44;}")
        else:
            return item.text()

    def check_authentication(self, change):
        hospital.execute("select User_Code from user where user.User_Code=%s and user.user_password=%s",
                         (change.usercode, change.password))
        user = hospital.fetchone()
        if user:
            hospital.execute("select Role_Name from role natural join user_role where user_Code = %s", (change.usercode,))
            role = hospital.fetchone()[0]

            if role:
                if role == "admin":
                    pass
                # go to admin page
                elif role == "patient":
                    pass
                # go to patient page
                elif role == "doctor":
                    change.change_page(change, 6)
                # go to doctor page
                elif role == "nurse":
                    change.change_page(change, 4)
                elif role == "receptionist":
                    change.change_page(change, 10)
                # go to receptionist page
                elif role == "accountant":
                    pass
                # go to accountant page
                elif role == "pharmacist":
                    change.change_page(change, 14)
                # go to pharmacist page
                elif role == "lab_staff":
                    pass
                # go to lab staff page
            else:
                print("You are not authorized yet wait for Admin to activate your account!!!")
        else:
            print("Authentication failed!\n Wrong username or password!")
