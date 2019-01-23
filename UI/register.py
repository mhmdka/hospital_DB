from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QComboBox
from packages.model import hospital, mydb
import smtplib


class register(QMainWindow):
    def __init__(self):
        super(register, self).__init__()
        self.registered = False

    def email(self, username, email_address):
        message = """Subject: Your username for login

        Hi {username}, your username for login is {user_code}"""

        name = username
        print(name)
        query = "select last_insert_id()"
        hospital.execute(query)
        user_code = hospital.fetchone()[0]
        email = email_address
        try:
            from_address = "moh.kahani@gmail.com"
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(from_address, "11kahani")
            server.sendmail(from_address, email, message.format(username=name, user_code=user_code))
            server.close()
            print('Email sent!')
        except:
            print("something went wrong!!")

    def register_page_logic(self, change, usercode):
        login_button = change.main_window.findChild(QPushButton, "RegisterPageLoginButton")
        login_button.clicked.connect(lambda: change.change_page(change, 1))

        register_button = change.main_window.findChild(QPushButton, "RegisterPageRegisterButton")
        register_button.clicked.connect(lambda: self.send_data_to_database(change, "RegisterPage"))
        if self.registered:
            register_button.clicked.connect(lambda: change.change_page(change, 1))
        self.registered = False

    @pyqtSlot()
    def send_data_to_database(self, change, string):
        print("sending data registeration")
        username_text_edit = change.main_window.findChild(QLineEdit, "RegisterPageUsernameLineEdit")
        password_text_edit = change.main_window.findChild(QLineEdit, "RegisterPagePasswordLineEdit")
        password_confirm_text_edit = change.main_window.findChild(QLineEdit, "RegisterPageConfirmPasswordLineEdit")
        email_text_edit = change.main_window.findChild(QLineEdit, "RegisterPageEmailLineEdit")
        phone_text_edit = change.main_window.findChild(QLineEdit, "RegisterPagePhoneNumberLineEdit")

        items = change.main_window.findChildren(QLineEdit)
        combo = change.main_window.findChild(QComboBox, "RegisterPageComboBox")

        flag = True
        for item in items:
            if string in item.objectName():
                if item.text() == "" and "Field" not in item.placeholderText():
                    text = item.placeholderText()
                    item.setPlaceholderText("Fill Field: " + text)
                    item.setStyleSheet("QLineEdit{ "
                                       "border:none;"
                                       "color:white;"
                                       "border-radius:5;"
                                       "background-color:#af2b44;}")
                    flag = False
        if combo.currentText() == "":
            print("you have to choose a role")
            return

        if password_confirm_text_edit.text() != password_text_edit.text():
            print("confirm password does not match")
            return

        if flag:
            try:
                query = "insert into user(Username,user_password,Phone_Number,`E-Mail`,isVerified) values(%s,%s,%s,%s,0)"
                val = (username_text_edit.text(), password_text_edit.text(), phone_text_edit.text(), email_text_edit.text())
                hospital.execute(query, val)
            except Exception as e:
                print(e)
                return
            mydb.commit()
            self.email(username_text_edit.text(), email_text_edit.text())
            print("you are registered! please wait for verification!!!!")
            hospital.execute("select role_ID from role where Role_Name=%s", (combo.currentText(),))
            role_id = hospital.fetchone()[0]
            hospital.execute(" insert into user_role(user_Code, role_ID) values(last_insert_id(),%s)", (role_id,))
            mydb.commit()
            self.registered = True


