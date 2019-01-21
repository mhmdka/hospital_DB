from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QLineEdit,QPushButton,QComboBox

class register(QMainWindow):
     def __init__(self):
         super(register,self).__init__()
         
     def register_page_logic(self,main_window,stacked_widget):        
        login_button = main_window.findChild(QPushButton,"RegisterPageLoginButton")
        login_button.clicked.connect(lambda: main_window.change_page(stacked_widget,0))
        
        register_button = main_window.findChild(QPushButton,"RegisterPageRegisterButton")
        register_button.clicked.connect(lambda: self.send_data_to_database(main_window,"RegisterPage"))
     
     @pyqtSlot()
     def send_data_to_database(self,main_window,string):
        items = main_window.findChildren(QLineEdit)
        combo = main_window.findChild(QComboBox)
        for item in items:
            if string in item.objectName():
                if item.text() == "" and "Field" not in item.placeholderText():
                         text = item.placeholderText()
                         item.setPlaceholderText("Fill Field: " + text)
                         item.setStyleSheet("QLineEdit{ "
                                                       "border:none;"
                                                       "color:white;"
                                                       "border-radius:5;"
                                                       "background-color:#af2b44;}")
          
                                                      
                else:
                    print(item.text())
                
        if(combo.currentText() == ""):
            print("Empty")