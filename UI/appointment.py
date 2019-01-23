from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTableWidget, QMessageBox, QListView, QLabel, QTableWidgetItem

from packages.model import hospital


class appointment(QMainWindow):
    def __init__(self):
        super(appointment, self).__init__()

    def appointment_logic_page(self, change, usercode):

        table = change.main_window.findChild(QTableWidget, "DoctorAppointmentsPageTableWidget")
        table.cellClicked.connect(lambda: self.delete_cell(table, table.currentRow(), table.currentColumn()))
        self.get_date(table, usercode)

    @pyqtSlot()
    def show_patient_drog_history(self, username):
        QMessageBox.information(self,
                                'Patient Drug History',
                                self.get_drugs(username),
                                QMessageBox.Ok)

    def delete_cell(self, table, row_selected, column_selected):
        if (column_selected == table.columnCount() - 1):
            table.removeRow(row_selected)
            self.send_data_to_database()

    def add_cell(self, data, change):
        table = change.main_window.findChild(QTableWidget, "DoctorAppointmentsPageTableWidget")
        table.insertRow(table.rowCount())
        for i in range(len(data)):
            if i == 2:
                button = QPushButton(str(data[2]))
                button.setStyleSheet("QPushButton{"
                                     "background-color: rgba(255, 255, 255, 50);"
                                     "color:rgb(0,0,0)}")
                table.setCellWidget(table.rowCount() - 1, 2, button)
                button.clicked.connect(lambda: self.show_patient_drog_history(data[2]))
                continue
            item = QTableWidgetItem(data[i])
            table.setItem(table.rowCount() - 1, i, item)

    def send_data_to_database(self):
        pass


    def get_date(self, table, username):
        hospital.execute("select date_appointment,time_appointment,Patient_UserCode,Username "
                         "from appointment, user where "
                         "appointment.Patient_UserCode = user.User_Code and Doctor_UserCode=%s", (username,))
        appointments = hospital.fetchall()
        for i in range(len(appointments)):
            table.insertRow(i)
        for i in range(len(appointments)):
            for j in range(4):
                if j == 2:
                    button = QPushButton(str(appointments[i][2]))
                    button.setStyleSheet("QPushButton{"
                                         "background-color: rgba(255, 255, 255, 50);"
                                         "color:rgb(0,0,0)}")
                    table.setCellWidget(i, 2, button)
                    button.clicked.connect(lambda: self.show_patient_drog_history(appointments[i][2]))
                    continue
                text = QTableWidgetItem(str(appointments[i][j]))
                table.setItem(i, j, text)

    def get_drugs(self, username):
        hospital.execute("select drug.Drug_ID,DrugName "
                         "from drug, has_drug, given, prescription where given.Patient_UserCode =%s "
                         "and given.PrescriptionID = prescription.PrescriptionID "
                         "and prescription.DrugFlag = true "
                         "and ExamineFlag = false "
                         "and has_drug.Drug_ID = drug.Drug_ID "
                         "and has_drug.Prescription_ID = given.PrescriptionID", (username,))

        drugs = hospital.fetchall()
        drug_string = ""

        for i in range(len(drugs)):
            drug_string = drug_string + str(i+1)+":"+drugs[i][1]+"("+str(drugs[i][0])+")"+"\n"

        return drug_string
