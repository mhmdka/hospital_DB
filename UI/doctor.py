from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QLineEdit,QPushButton,QTableWidget,QVBoxLayout,QListView,QLabel,QTableWidgetItem
from PyQt5.QtGui import QStandardItem,QStandardItemModel

class doctor(QMainWindow):
     def __init__(self):
         super(doctor,self).__init__()
    
    
     def doctor_page_logic(self,main_window,stacked_widget):
        self.inbox_page_logic(main_window) 
        
     def inbox_page_logic(self,main_window):
         table = main_window.findChild(QTableWidget,"tableWidget") 
         for i in range(10):
             table.insertRow(i)
             
         for i in range(10):
             for j in range(4):
                 line = QTableWidgetItem("Fuck")
                 table.setItem(i, j, line);

         
        
     def get_data_from_database(self,main_window):
         item = QStandardItem()
         item.setCheckable(True)
         list_view = main_window.findChild(QListView,"DoctorInboxPageListView")
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
         
         
         
         
    