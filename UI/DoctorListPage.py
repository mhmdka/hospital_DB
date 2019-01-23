from packages.model import hospital
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem
class DoctorListPage:

    def __init__(self):
        super(DoctorListPage, self).__init__()

    def doctorlist_page_logic(self, change):
        table = change.main_window.findChild(QTableWidget, "DoctorsListPageTableWidget")
        self.get_data(table)

        back_button = change.main_window.findChild(QPushButton, "DoctorListPageBackButton")
        back_button.clicked.connect(lambda: change.change_page(change, 10))

    def get_data(self, table):
        hospital.execute("select user.User_Code,Username,Phone_Number,`E-Mail` from user,"
                         "user_role where user.User_Code = user_role.user_Code "
                         "and user_role.role_ID = 3 and user.isVerified=0;")
        doctors = hospital.fetchall()
        for i in range(len(doctors)):
            table.insertRow(i)

        for i in range(len(doctors)):
            for j in range(4):
                print(i)
                text = QTableWidgetItem(str(doctors[i][j]))
                table.setItem(i, j, text)
