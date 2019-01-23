from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QTableWidget, QVBoxLayout, QListView, QLabel, \
    QTableWidgetItem
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from UI.appointment import appointment


class doctor(QMainWindow):
    def __init__(self):
        super(doctor, self).__init__()

    def doctor_page_logic(self, change, usercode):
        appointment_button = change.main_window.findChild(QPushButton, "DoctorPageAppointmentButton")
        appointment_button.clicked.connect(lambda: change.change_page(change, 9))
        table = change.main_window.findChild(QTableWidget, "DoctorPageTableWidget")
        table.cellClicked.connect(lambda: self.delete_cell(table, table.currentRow(), table.currentColumn(), change))
        # self.inbox_page_logic(change)

    def inbox_page_logic(self, change):
        table = change.main_window.findChild(QTableWidget, "tableWidget")
        for i in range(10):
            table.insertRow(i)

        for i in range(10):
            for j in range(4):
                line = QTableWidgetItem("Fuck")
                table.setItem(i, j, line)


    def delete_cell(self, table, row_selected, column_selected, change):
        if column_selected == table.columnCount() - 1:
            print("delete")
            table.removeRow(row_selected)
        elif column_selected == table.columnCount() - 2:
            print("Accept")
            data = []
            for i in range(table.columnCount() - 2):
                data.append(table.item(row_selected, i).text())
            table.removeRow(row_selected)
            appointmentPage = appointment()
            appointmentPage.add_cell(data, change)


def get_data_from_database(self, main_window):
    item = QStandardItem()
    item.setCheckable(True)
    list_view = main_window.findChild(QListView, "DoctorInboxPageListView")
    model = QStandardItemModel(list_view)
    foods = [
        '12/12/1397',
        '11/08/2013',
        '04/03/2254',
        '01/05/2008',
        '02/02/1397'
    ]

    for food in foods:
        item = QStandardItem(food)
        item.setCheckable(True)
        model.appendRow(item)

    list_view.setModel(model)
