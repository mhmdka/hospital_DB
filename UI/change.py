from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from packages.model import hospital
from PyQt5.QtCore import pyqtSlot

from UI.doctor import doctor
from UI.nurse import nurse
from UI.forget import forget
from UI.register import register
from UI.login import login


registerPage = None
forgetPage = None
nursePage = None
doctorPage = None
loginPage = None


class Change:
    def __init__(self):
        self.main_window = None
        self.stacked_widget = None
        self.usercode = ""

    @pyqtSlot()
    def change_page(self, change, i):
        print("we are in change")
        change.stacked_widget.setCurrentIndex(i)
        if i == 1:
            global loginPage
            if loginPage == None:
                loginPage = login()
            loginPage.login_page_logic(change)
        if i == 2:
            global registerPage
            if registerPage == None:
                registerPage = register()
            registerPage.register_page_logic(change, change.usercode)
        elif i == 3:
            global forgetPage
            if forgetPage == None:
                forgetPage = forget()
            forgetPage.forget_page_logic(change, change.usercode)
        elif i == 4:
            global nursePage
            if nursePage == None:
                nursePage = nurse()
            nursePage.send_nurse_report_logic_page(change, change.usercode)
