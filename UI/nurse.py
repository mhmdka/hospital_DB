from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QLineEdit,QPushButton,QScrollArea,QVBoxLayout

class nurse(QMainWindow):
     def __init__(self):
         super(nurse,self).__init__()
         
     def send_nurse_report_logic_page(self,main_window,stacked_widget):
        submit_button = main_window.findChild(QPushButton,"NursePageSubmitReportButton")
        submit_button.clicked.connect(lambda: self.send_data_to_database(main_window,"NursePage"))
        
        records_button = main_window.findChild(QPushButton,"NursePageResportsRecordButton")
        records_button.clicked.connect(lambda: main_window.change_page(stacked_widget,4))
    
     
     @pyqtSlot()
     def send_data_to_database(self,main_window,string):
         items = main_window.findChildren(QLineEdit)    
         for item in items:
             if string in item.objectName():
                 item.setStyleSheet("QLineEdit{ "
                                                   "border:none;"
                                                   "border-radius:5;"
                                                   "background-color:#af2b44;}")
             else:
                 print(item.text())