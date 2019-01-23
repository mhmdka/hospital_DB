from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTableWidget, QLineEdit, QListView, QLabel, QTableWidgetItem

from packages.model import hospital, mydb


class pharmacist(QMainWindow):
    def __init__(self):
        super(pharmacist, self).__init__()

    def pharmacy_logic_page(self,change,usercode):
        print("Pharmacy")
        table = change.main_window.findChild(QTableWidget, "PharmacistPageTableWidget")
        self.get_data(table)
        searchTextEdit = change.main_window.findChild(QLineEdit,"PharmacistPageLineEdit")
        submit_button = change.main_window.findChild(QPushButton, "PharmacistPageSubmitButton")
        submit_button.clicked.connect(lambda: self.get_data_search(table,searchTextEdit))
        add_button = change.main_window.findChild(QPushButton, "PharmacistPageAddButton")
        add_button.clicked.connect(lambda: self.add_cell(table))
        table.cellClicked.connect(lambda: self.delete_cell(table, table.currentRow(), table.currentColumn()))
    #irad dare!
    def delete_cell(self, table, row_selected, column_selected):
        if (column_selected == table.columnCount() - 1):
            data = []
            for i in range(table.columnCount() - 1):
                print("i: ", i)
                text = table.item(row_selected, i).text()
                data.append(text)
                print("\n\n\n")
                print(data[i])
                try:
                    hospital.execute(
                        "delete from drug where DrugName=%s and ExpirationDate=%s and Price=%s"(data[0],data[1],data[3]))
                except Exception as e:
                    print(e)
                mydb.commit()
            table.removeRow(row_selected)


    def add_cell(self, table):
        data = []
        print(table.rowCount())

        for i in range(table.columnCount()-1):
            print("i: ", i)
            if (table.item(table.rowCount() - 1, i) == None):
                return
            text = table.item(table.rowCount() - 1, i).text()
            data.append(text)
            print(data[i])

            try:
                hospital.execute(
                    "insert into drug(DrugName, ExpirationDate, Price) "
                    "values (%s,%s,%s);", (data[0], data[1], data[2]))
            except Exception as e:
                print(e)
            mydb.commit()
        table.insertRow(table.rowCount())

    def get_data(self, table):
        hospital.execute("select DrugName,ExpirationDate,Price from drug")
        drugs = hospital.fetchall()
        for i in range(len(drugs)):
            table.insertRow(i)

        for i in range(len(drugs)):
            for j in range(3):
                text = QTableWidgetItem(str(drugs[i][j]))
                table.setItem(i, j, text)
        table.insertRow(table.rowCount())


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
        item.setStyleSheet("QLine Edit{ "
                           "border:none;"
                           "border-radius:5;"
                           "background-color:white;}")

        hospital.execute("select DrugName,ExpirationDate,Price from drug where ExpirationDate > %s order by ExpirationDate asc",
                         (item.text(),))
        filters = hospital.fetchall()

        for i in range(table.rowCount() - 1):
            table.removeRow(i)
            print(table.rowCount())

        #
        # for i in range(len(filters)):
        #     table.insertRow(i)
        #
        # for i in range(len(filters)):
        #     for j in range(4):
        #         text = QTableWidgetItem(str(filters[i][j]))
        #         table.setItem(i, j, text)
        # print("successful")