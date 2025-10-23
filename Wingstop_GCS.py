# Wingstop GCS

# creating frontend
import pyqtgraph
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget
import sys

class MyWindow(QMainWindow):
    # creates and sizes a window
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(100,100,1800,900)
        self.setWindowTitle("Wing-Stop Ground Station")
        self.initUI()
    
    # creates the user interface
    def initUI(self):
        self.label=QtWidgets.QLabel(self)
        self.label.setText("Just Wing It")
        self.label.move(100,100)

        # code to create a push button
        self.release=QtWidgets.QPushButton(self)
        self.release.setText("Release Glider")
        # add function of what this button will do when it is clicked
        self.release.clicked.connect(self.released)

    # makes the button do something
    def released(self):
        self.label.setText("you released the glider")
        self.update()

    def update(self):
        self.label.adjustSize()

# function to open a ground station window
def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
