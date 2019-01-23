from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QPushButton, QTableWidget, QMessageBox, QListView, QLabel, \
    QTableWidgetItem, QLineEdit
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtGui import QIcon, QPixmap

from packages.model import hospital, mydb


class Receptionist:
    def __init__(self):
        super(Receptionist, self).__init__()

    def receptionist_logic_page(self, change):
        table = change.main_window.findChild(QTableWidget, "ReceptionistPageTableWidget")
        self.get_data(table)

        doctor_button = change.main_window.findChild(QPushButton, "ReceptionistPageDoctorsButton")
        doctor_button.clicked.connect(lambda: change.change_page(change, 17))

        search_doctor_id = change.main_window.findChild(QLineEdit, "ReceptionistPageSearchLineEdit")

        filter_button = change.main_window.findChild(QPushButton, "ReceptionistPageFilterButton")
        filter_button.clicked.connect(lambda: self.get_data_search(table, search_doctor_id))

        add_button = change.main_window.findChild(QPushButton, "ReceptionistPageAddButton")
        if (add_button != None):
            add_button.clicked.connect(lambda: self.add_cell(table))

    def add_cell(self, table):
        data = []
        print(table.rowCount())

        for i in range(table.columnCount()):
            print("i: ", i)
            if (table.item(table.rowCount() - 1, i) == None):
                return
            text = table.item(table.rowCount() - 1, i).text()
            data.append(text)
            print(data[i])

        try:
            hospital.execute(
                "insert into appointment(date_appointment,time_appointment,Doctor_UserCode, Patient_UserCode) "
                "values (%s,%s,%s,%s);", (data[0], data[1], data[2], data[4]))
        except Exception as e:
            print(e)
        mydb.commit()
        table.insertRow(table.rowCount())

    def send_data_to_database(self):
        pass

    def get_data(self, table):
        hospital.execute("select date_appointment,time_appointment,Doctor_UserCode,Username,Patient_UserCode "
                         "from appointment, user where appointment.Doctor_UserCode = user.User_Code")
        appointments = hospital.fetchall()
        for i in range(len(appointments)):
            table.insertRow(i)

        for i in range(len(appointments)):
            for j in range(4):
                text = QTableWidgetItem(str(appointments[i][j]))
                table.setItem(i, j, text)

    def get_data_search(self, table, item):

        if item.text() == "":
            item.setStyleSheet("QLineEdit{ "
                               "border:none;"
                               "border-radius:5;"
                               "background-color:#af2b44;}"
                               "QLineEdit:focus {"
                               "border:none;"
                               "border-radius:5;"
                               "background-color:white;}")
            return
        item.setStyleSheet("QLineEdit{ "
                           "border:none;"
                           "border-radius:5;"
                           "background-color:white;}")

        hospital.execute("select date_appointment,time_appointment,Doctor_UserCode,Username,Patient_UserCode "
                         "from appointment, user where appointment.Doctor_UserCode = user.User_Code and User_Code=%s",
                         (item.text(),))
        filters = hospital.fetchall()
        for i in range(table.rowCount() - 1):
            table.removeRow(i)
        print(table.rowCount())

        for i in range(len(filters)):
            table.insertRow(i)

        for i in range(len(filters)):
            for j in range(4):
                text = QTableWidgetItem(str(filters[i][j]))
                table.setItem(i, j, text)
        print("successful")
