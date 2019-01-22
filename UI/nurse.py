from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QScrollArea, QVBoxLayout, QLabel
from packages.model import hospital


class nurse(QMainWindow):
    def __init__(self):
        super(nurse, self).__init__()
        self.current = 0
        self.prev = 0

    def send_nurse_report_logic_page(self, change, usercode):
        submit_button = change.main_window.findChild(QPushButton, "NursePageSubmitReportButton")
        submit_button.clicked.connect(lambda: self.send_data_to_database(change.main_window, "NursePage"))

        nurse_username = change.main_window.findChild(QLabel, "NursePageUsername")

        print("username is:", usercode)
        hospital.execute("select Username from user where User_Code = %s", (usercode,))
        username = hospital.fetchone()[0]
        nurse_username.setText(username)
        print(nurse_username.text())

        records_button = change.main_window.findChild(QPushButton, "NursePageResportsRecordButton")
        records_button.clicked.connect(lambda: change.change_page(change, 5))

    @pyqtSlot()
    def send_data_to_database(self, main_window, string):
        items = main_window.findChildren(QLineEdit)
        for item in items:
            if string in item.objectName():
                item.setStyleSheet("QLineEdit{ "
                                   "border:none;"
                                   "border-radius:5;"
                                   "background-color:#af2b44;}")
            else:
                print(item.text())
