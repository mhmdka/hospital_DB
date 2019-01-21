import sys

from PyQt5.QtCore import pyqtSlot

from UI.register import register
from UI.forget import forget
from UI.login import login
from UI.nurse import nurse
from UI.doctor import doctor

from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

global registerPage
global forgetPage
global nursePage
global doctorPage

registerPage = None
forgetPage = None
nursePage = None
doctorPage= None

class main(QMainWindow):   
    def __init__(self):
        super(main,self).__init__()
        loadUi('UI.ui', self)
        
        stacked_widget = self.findChild(QStackedWidget, "StackedWidget")
        
        #nursePage = nurse()
        #nursePage.send_nurse_report_logic_page(self,stacked_widget)

        # doctorPage = doctor()
        # doctorPage.doctor_page_logic(self, stacked_widget)


        loginPage = login()
        loginPage.login_page_logic(self, stacked_widget)
    
    @pyqtSlot()
    def change_page(self,stacked_widget,i):
        stacked_widget.setCurrentIndex(i)
        if(i==1):
            global registerPage
            if(registerPage == None):
                registerPage = register()
            registerPage.register_page_logic(self,stacked_widget)
        elif(i==2):
            global forgetPage
            if(forgetPage == None):
                forgetPage = forget()
            forgetPage.forget_page_logic(self,stacked_widget)
        elif(i==4):
            global nursePage
            if(nursePage == None):
                nursePage = nurse()
            nursePage.records_page_logic(self,stacked_widget)
        
app=QApplication(sys.argv)
app_icon = QIcon("UI.png")
app.setWindowIcon(app_icon)
widget=main()
widget.show()
sys.exit(app.exec_())