import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

from UI.change import Change


change = None

class main(QMainWindow):   
    def __init__(self):
        super(main, self).__init__()
        loadUi('UI.ui', self)
        
        stacked_widget = self.findChild(QStackedWidget, "StackedWidget")
        change = Change()
        change.stacked_widget = stacked_widget
        change.main_window = self
        welcomeButton = self.findChild(QPushButton, "WelcomePageButton")
        welcomeButton.clicked.connect(lambda: change.change_page(change, 1))


        
app = QApplication(sys.argv)
app_icon = QIcon("UI.png")
app.setWindowIcon(app_icon)
widget = main()
widget.show()
sys.exit(app.exec_())
