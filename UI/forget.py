from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from packages.model import hospital
import smtplib


class forget(QMainWindow):
    def __init__(self):
        super(forget, self).__init__()

    def email(self, email_address, user_code, user_password):
        message = """Subject: Your password for login

        Hi! your username is {user_code} and  your password for login is {password}"""

        email = email_address
        try:
            from_address = "moh.kahani@gmail.com"
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(from_address, "11kahani")
            server.sendmail(from_address, email, message.format(user_code=user_code, password=user_password))
            server.close()
            print('Email sent!')
        except:
            print("something went wrong!!")

    def forget_page_logic(self, change):
        login_button = change.main_window.findChild(QPushButton, "ForgetPageLoginButton")
        login_button.clicked.connect(lambda: change.change_page(change, 1))

        register_button = change.main_window.findChild(QPushButton, "ForgetPageSendButton")
        register_button.clicked.connect(lambda: self.send_data_to_database(change, "ForgetPage"))
        register_button.clicked.connect(lambda: change.change_page(change, 1))

    @pyqtSlot()
    def send_data_to_database(self, change, string):

        print("sending data forget")
        email_text_edit = change.main_window.findChild(QLineEdit, "ForgetPageLineEdit")
        items = change.main_window.findChildren(QLineEdit)
        flag = True
        for item in items:
            if string in item.objectName():
                if item.text() == "" and "Field" not in item.placeholderText():
                    text = item.placeholderText()
                    item.setPlaceholderText("Fill Field: " + text)
                    item.setStyleSheet("QLineEdit{ "
                                       "border:none;"
                                       "border-radius:5;"
                                       "background-color:#af2b44;}")
                    flag = False

        hospital.execute("select User_Code,user_password from user where `E-Mail`=%s", (email_text_edit.text(),))
        result = hospital.fetchone()
        if not result:
            print("there is no email address registered as you requested!!")
            return
        user_code = result[0]
        user_password = result[1]
        if flag:
            self.email(email_text_edit.text(), user_code, user_password)

