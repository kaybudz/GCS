# importing necessary libraries
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, mkPen
import numpy

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        # creating main window
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1255, 693)
        MainWindow.resize(1920,1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        
        # creating graph frame
        self.graph_frame = QtWidgets.QFrame(self.centralwidget)
        #self.graph_frame.setGeometry(QtCore.QRect(380, 100, 851, 521))
        self.graph_frame.setGeometry(QtCore.QRect(582, 156, 1303, 811))
        #self.graph_frame.setFrameShape(QtWidgets.QFrame.Box)
        #self.graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        #self.graph_frame.setLineWidth(5)
        self.graph_frame.setObjectName("graph_frame")

        # creating layout of graphs
        self.gridLayout = QtWidgets.QGridLayout(self.graph_frame)
        self.gridLayout.setContentsMargins(11, -1, -1, -1)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")

        # altitude graph
        self.altitude = PlotWidget(self.graph_frame)
        self.altitude.setObjectName("altitude")
        self.gridLayout.addWidget(self.altitude, 0, 0, 1, 1)
        self.altitude.setBackground("w")
        self.altitude.setTitle("Altitude vs Time")
        self.altitude.setLabel("left", "Altitude (m)")
        self.altitude.setLabel("bottom", "Time (min)")
        self.altitude.showGrid(x=True, y=True)
        #update_plot(self, altitude)

        # air speed graph
        self.speed = PlotWidget(self.graph_frame)
        self.speed.setObjectName("speed")
        self.gridLayout.addWidget(self.speed, 0, 1, 1, 1)
        self.speed.setBackground("w")
        self.speed.setTitle("Air Speed vs Time")
        self.speed.setLabel("left", "Air Speed (m/s)")
        self.speed.setLabel("bottom", "Time (min)")
        self.speed.showGrid(x=True, y=True)

        # tilt graph
        self.tilt = PlotWidget(self.graph_frame)
        self.tilt.setObjectName("tilt")
        self.gridLayout.addWidget(self.tilt, 0, 2, 1, 1)
        self.tilt.setBackground("w")
        self.tilt.setTitle("Tilt X vs Tilt Y")
        self.tilt.setLabel("left", "Tilt Y (deg)")
        self.tilt.setLabel("bottom", "Tilt X (deg)")
        self.tilt.showGrid(x=True, y=True)

        # temperature graph
        self.temperature = PlotWidget(self.graph_frame)
        self.temperature.setObjectName("temperature")
        self.gridLayout.addWidget(self.temperature, 1, 0, 1, 1)
        self.temperature.setBackground("w")
        self.temperature.setTitle("Temperature vs Time")
        self.temperature.setLabel("left", "Temperature (°C)")
        self.temperature.setLabel("bottom", "Time (min)")
        self.temperature.showGrid(x=True, y=True)

        # pressure graph
        self.pressure = PlotWidget(self.graph_frame)
        self.pressure.setObjectName("pressure")
        self.gridLayout.addWidget(self.pressure, 1, 1, 1, 1)
        self.pressure.setBackground("w")
        self.pressure.setTitle("Pressure vs Time")
        self.pressure.setLabel("left", "Pressure (Pa)")
        self.pressure.setLabel("bottom", "Time (min)")
        self.pressure.showGrid(x=True, y=True)

        # sets up timer for graphs
        #self.timer = QtCore.QTimer()
        #self.timer.setInterval(300)
        #self.timer.timeout.connect(self.update_plot)
        #self.timer.start()

        # location widget (hopefully a map figure out how to code that)
        self.location = QtWidgets.QWidget(self.graph_frame)
        self.location.setObjectName("location")
        self.gridLayout.addWidget(self.location, 1, 2, 1, 1)
        #self.location.setBackground("w")

        # creating button frame
        self.button_frame = QtWidgets.QFrame(self.centralwidget)
        #self.button_frame.setGeometry(QtCore.QRect(30, 530, 321, 87))
        self.button_frame.setGeometry(QtCore.QRect(46, 825, 491, 135))
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")

        # creating layout for buttons
        self.gridLayout_2 = QtWidgets.QGridLayout(self.button_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # beacon button
        self.beacon = QtWidgets.QPushButton(self.button_frame)
        self.beacon.setObjectName("beacon")
        self.gridLayout_2.addWidget(self.beacon, 0, 0, 1, 1)

        # calibrate button
        self.calibrate = QtWidgets.QPushButton(self.button_frame)
        self.calibrate.setObjectName("calibrate")
        self.gridLayout_2.addWidget(self.calibrate, 0, 1, 1, 1)

        # release button
        self.release = QtWidgets.QPushButton(self.button_frame)
        self.release.setObjectName("release")
        self.gridLayout_2.addWidget(self.release, 1, 0, 1, 1)

        # transmit button
        self.transmit = QtWidgets.QPushButton(self.button_frame)
        self.transmit.setObjectName("transmit")
        self.gridLayout_2.addWidget(self.transmit, 1, 1, 1, 1)

        # creating table for live data
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        #self.tableWidget.setGeometry(QtCore.QRect(60, 140, 251, 371))
        self.tableWidget.setGeometry(QtCore.QRect(92, 218, 384, 578))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        #self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        #self.tableWidget.resizeColumnsToContents()
        
        # creating rows and columns of the table
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        
        # THESE CURRENTLY HAVE NO FUNCTION FIGURE OUT IF THEY NEED TO FUNCTION
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1255, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # determing what button names are
    # determing what table row and column names are
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.beacon.setText(_translate("MainWindow", "Start Beacon"))
        self.calibrate.setText(_translate("MainWindow", "Calibrate"))
        self.release.setText(_translate("MainWindow", "Release Glider"))
        self.transmit.setText(_translate("MainWindow", "Transmit Telemetry"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Team ID"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Packet Count"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Packets Recieved"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Software State"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Payload State"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Voltage"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Latitude"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Altitude"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data"))

    def update_plot(self):
        self.time = self.time[1:]
        self.time.append(self.time[-1] + 1)
        self.graph = self.graph[1:]
        self.graph.append(randint(20, 40))
        self.line.setData(self.time, self.graph)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
