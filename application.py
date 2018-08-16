
#Importing library
from PyQt5 import QtGui, QtWidgets
import os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from MTIAssignment import getCenterAndDistance, load_data



class PrettyWidget(QtWidgets.QWidget):
   
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(600,300, 1000, 600)
        self.center()
        self.setWindowTitle('MTI GUI')     
        
        #Grid Layout
        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)
        
        #Canvas and Toolbar
        self.figure = plt.figure(figsize=(15,5))    
        self.canvas = FigureCanvas(self.figure)     
        #self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.canvas, 2,0,1,2)
        #grid.addWidget(self.toolbar, 1,0,1,2)
            
        #Import CSV Button
        btn1 = QtWidgets.QPushButton('Import text file', self)
        btn1.resize(btn1.sizeHint()) 
        btn1.clicked.connect(self.getCSV)
        grid.addWidget(btn1, 0,0)
        
        self.show()
    
    
    def getCSV(self):
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, 
                                                       'Single File',
                                                       '~/Desktop/PyRevolution/PyQt4',
                                                       '*.txt')
        print("****")
        print(filePath[0])
        df = load_data(filePath[0])
        
        #get distance and center for intersection
        
        
        
        ax1 = self.figure.add_subplot(111)
        ax1.plot(df["Wavelength"], df["Transmission"])
        ax1.set_xlabel('Wavelength')
        ax1.set_ylabel('Transmission')

        #plt(figure)' 
        self.canvas.draw()
        
        
        print(getCenterAndDistance(filePath[0]))
    
        print("*****")
        """
        fileHandle = open(filePath, 'r')
        line = fileHandle.readline()[:-1].split(',')
        for n, val in enumerate(line):
            newitem = QtWidgets.QTableWidgetItem(val)
            self.table.setItem(0, n, newitem)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()    
    """
    
    def plot(self):
        y = []
        for n in range(9):
            try:
                y.append(float(self.table.item(0, n).text()))
            except:
                y.append(np.nan)
        plt.cla()
        ax = self.figure.add_subplot(111)
        ax.plot(y, 'r.-')
        ax.set_title('Table Plot')
        self.canvas.draw()
    
    
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = PrettyWidget()
    app.exec_()


if __name__ == '__main__':
    main()