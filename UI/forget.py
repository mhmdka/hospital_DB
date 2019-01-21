from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QLineEdit,QPushButton

class forget(QMainWindow):
     def __init__(self):
         super(forget,self).__init__()
     
     def forget_page_logic(self,main_window,stacked_widget):
        login_button = main_window.findChild(QPushButton,"ForgetPageLoginButton")
        login_button.clicked.connect(lambda: main_window.change_page(stacked_widget,0))
        
        register_button = main_window.findChild(QPushButton,"ForgetPageSendButton")
        register_button.clicked.connect(lambda: self.send_data_to_database(main_window,"ForgetPage"))
    
     @pyqtSlot()
     def send_data_to_database(self,main_window,string):
         items = main_window.findChildren(QLineEdit)    
         for item in items:
             if string in item.objectName():
                 if item.text() == "" and "Field" not in item.placeholderText():
                      text = item.placeholderText()
                      item.setPlaceholderText("Fill Field: " + text)
                      item.setStyleSheet("QLineEdit{ "
                                                   "border:none;"
                                                   "border-radius:5;"
                                                   "background-color:#af2b44;}")
                 else:
                     print(item.text())