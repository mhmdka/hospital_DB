from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from packages.model import hospital
from PyQt5.QtCore import pyqtSlot

from UI.doctor import doctor
from UI.nurse import nurse
from UI.forget import forget
from UI.register import register
from UI.login import login
from UI.DoctorListPage import DoctorListPage
from UI.receptionist import Receptionist
from UI.appointment import appointment
from UI.pharmacist import pharmacist
registerPage = None
forgetPage = None
nursePage = None
doctorPage = None
loginPage = None
doctorlistPage = None
receptionistPage = None
appointmentPage = None
pharmacistPage = None

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
            forgetPage.forget_page_logic(change)
        elif i == 4:
            global nursePage
            if nursePage == None:
                nursePage = nurse()
            nursePage.send_nurse_report_logic_page(change, change.usercode)

        elif i == 6:
            global doctorPage
            if doctorPage == None:
                doctorPage = doctor()
            doctorPage.doctor_page_logic(change, change.usercode)

        elif i == 9:
            global appointmentPage
            if appointmentPage == None:
                appointmentPage = appointment()
            appointmentPage.appointment_logic_page(change, change.usercode)

        elif i == 10:
            global receptionistPage
            if receptionistPage == None:
                receptionistPage = Receptionist()
            receptionistPage.receptionist_logic_page(change)

        elif i == 14:
            global pharmacistPage
            if pharmacistPage == None:
                pharmacistPage = pharmacist()
            pharmacistPage.pharmacy_logic_page(change,change.usercode)

        elif i == 17:
            global doctorlistPage
            if doctorlistPage == None:
                doctorlistPage = DoctorListPage()
            doctorlistPage.doctorlist_page_logic(change)