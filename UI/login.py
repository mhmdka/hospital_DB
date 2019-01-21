from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from packages.model import hospital

class login(QMainWindow):

     def __init__(self):
         super(login,self).__init__()
         self.usercode = 0
         self.password = 0
         
     def login_page_logic(self,main_window,stacked_widget):
        login_button = main_window.findChild(QPushButton,"LoginPageLoginButton")
        login_button.clicked.connect(lambda: self.send_data_to_database(main_window,"LoginPage",stacked_widget))
        
        register_button = main_window.findChild(QPushButton,"LoginPageRegisterButton")
        register_button.clicked.connect(lambda: main_window.change_page(stacked_widget, 1))
        
        forget_button = main_window.findChild(QPushButton,"LoginPageForgetButton")
        forget_button.clicked.connect(lambda: main_window.change_page(stacked_widget, 2))
       
     @pyqtSlot()
     def send_data_to_database(self, main_window, string, stacked_widget):
         print("Sending Data")
         login_text_edit = main_window.findChild(QLineEdit, "LoginPageUsernameLineEdit")
         password_text_edit = main_window.findChild(QLineEdit, "LoginPagePasswordLineEdit")
         self.usercode = self.get_data(login_text_edit)
         self.password = self.get_data(password_text_edit)
         
         if self.usercode != 0 and self.password != 0:
             self.check_authentication(main_window, stacked_widget)
         
     def get_data(item):
          if item.text() == "" and "Field" not in item.placeholderText():
              text = item.placeholderText()
              item.setPlaceholderText("Fill Field: " + text)
              item.setStyleSheet("QLineEdit{ "
                                           "border:none;"
                                           "border-radius:5;"
                                           "background-color:#af2b44;}")
          else:
             return item.text()
         
     def check_authentication(self,main_window,stacked_widget):
        hospital.execute("select User_Code from user where user.User_Code=%s and user.user_password=%s",
                         (self.usercode, self.password))
        user = hospital.fetchone()
        if user:
            hospital.execute("select Role_Name from user natural join user_role where user_Code = %s", (self.usercode,))
            role = hospital.fetchone()[0]

            if role:
                if role == "admin":
                    pass
                # go to admin page
                elif role == "patient":
                    pass
                # go to patient page
                elif role == "doctor":
                    pass
                # go to doctor page
                elif role == "nurse":
                    main_window(stacked_widget, 4)
                elif role == "receptionist":
                    pass
                # go to receptionist page
                elif role == "accountant":
                    pass
                # go to accountant page
                elif role == "pharmacist":
                    pass
                # go to pharmacist page
                elif role == "Lab_Staff":
                    pass
                #go to lab staff page
            else:
                print("You are not authorized yet wait for Admin to activate your account!!!")
        else:
            print("Authentication failed!\n Wrong username or password!")
         
              