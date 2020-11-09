from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
from modul1 import *
from modul2 import *
from ikony import *
from PyQt5.QtCore import pyqtSignal, QObject

class MainWindow(QMainWindow, QWidget,QObject) :
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(10)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Dialog')

        self.ikony = ChangeIcon(self)
        self.mod1 = CustomDialog(self)
        self.mod2 = CustomDialog2(self)
        self.ikony.changed.connect(self.changeIcon)
        #self.mod1.changed1.connect(self.paintEvent)
        self.mod2.changed2.connect(self.paintEvent)

        self.newAct1 = QAction('Kolor okna głównego', self,triggered=self.mod1_open)
        self.newAct2 = QAction('Ustaw koła', self,triggered=self.mod2_open)
        self.newAct3 = QAction('Zmień ikonę',self,triggered=self.mod3_open)
        fileMenu.addAction(self.newAct1)
        fileMenu.addAction(self.newAct2)
        fileMenu.addAction(self.newAct3)


        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Dialogi')
        self.show()

    def paintEvent(self, index):
        qp = QPainter(self)
        qp.setBrush(QColor(0, 200, 0))
        qp.drawRect(0, 0, 500, 400)
        diameter1 = self.mod2.slider1.value()
        x = (500 / 2) - (diameter1 / 2)
        y = (400 / 2) - (diameter1 / 2)

        colorID = self.mod1.combo.currentIndex()
        if colorID == 0:
            qp.setBrush(QColor(255, 0, 0))  # czerwony
        elif colorID == 1:
            qp.setBrush(QColor(0, 102, 0))  # zielony
        elif colorID == 2:
            qp.setBrush(QColor(153, 204, 255))
        elif colorID == 3:
            qp.setBrush(QColor(255, 255, 0))
        else:
            qp.setBrush(QColor(153, 204, 255))

        qp.drawEllipse(x, y, diameter1, diameter1)
        diameter2 = self.mod2.slider2.value()
        x = (500 / 2) - (diameter2 / 2)
        y = (400 / 2) - (diameter2 / 2)
        qp.setBrush(QColor(0, 200, 0))
        qp.drawEllipse(x, y, diameter2, diameter2)

    def mod1_open(self):
        self.mod1.show()
    def mod2_open(self):
        self.mod2.show()
    def mod3_open(self):
        self.ikony.show()


    def changeIcon(self, buttonID):
        if buttonID == '-2':
            self.icon = QIcon('happy.png')
            self.setWindowIcon(self.icon)
        elif buttonID == '-3':
            self.icon = QIcon('normal.png')
            self.setWindowIcon(self.icon)
        elif buttonID == '-4':
            self.icon = QIcon('sad.png')
            self.setWindowIcon(self.icon)

    def closeEvent(self, event):
        self.ikony.exit()
        self.mod1.exit()
        self.mod2.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    slider = MainWindow()
    sys.exit(app.exec_())



