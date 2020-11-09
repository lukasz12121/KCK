from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtCore import pyqtSignal


class ChangeIcon(QDialog) :

    changed = pyqtSignal(str)

    def __init__(self,parent=None, title=''):
        super(ChangeIcon, self).__init__()
        #self.initUI()
    #def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(10)

        #radio buttony
        self.buttonGroup1 = QButtonGroup(self)
        texts = ['Wesoła', 'Normalna','Smutna']
        self.radioFrame = QGroupBox(self)
        self.radioFrame.setGeometry(10,20,100,120)
        self.radioFrame.setStyleSheet("border: 1px solid gray;")
        self.radioFrame.setTitle('Zmień ikone')

        self.button1 = QRadioButton(texts[0],self)
        self.buttonGroup1.addButton(self.button1)
        self.button1.setChecked(True)
        self.button1.move(20,40)
        self.button1.toggled.connect(self.image1)
        self.button2 = QRadioButton(texts[1],self)
        self.buttonGroup1.addButton(self.button2)
        self.button2.move(20, 70)
        self.button2.toggled.connect(self.image2)
        self.button3 = QRadioButton(texts[2],self)
        self.buttonGroup1.addButton(self.button3)
        self.button3.move(20, 100)
        self.button3.toggled.connect(self.image3)
        self.buttonGroup1.setExclusive(True)

        #checkboxy
        self.buttonGroup2 = QButtonGroup(self)
        self.checkFrame = QGroupBox(self)
        self.checkFrame.setGeometry(10, 180, 100, 120)
        self.checkFrame.setStyleSheet("border: 1px solid gray;")
        self.checkFrame.setTitle('Zmień ikone')
        self.checkbox1 = QCheckBox(texts[0], self)
        self.checkbox1.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.checkbox1.setFocusPolicy(Qt.NoFocus)
        self.buttonGroup2.addButton(self.checkbox1)
        self.checkbox1.setChecked(True)
        self.checkbox1.move(20, 200)
        self.checkbox2 = QCheckBox(texts[1], self)
        self.checkbox2.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.checkbox2.setFocusPolicy(Qt.NoFocus)
        self.buttonGroup2.addButton(self.checkbox2)
        self.checkbox2.move(20, 230)
        self.checkbox3 = QCheckBox(texts[2], self)
        self.checkbox3.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.checkbox3.setFocusPolicy(Qt.NoFocus)
        self.buttonGroup2.addButton(self.checkbox3)
        self.checkbox3.move(20, 260)
        self.buttonGroup2.setExclusive(True)

        #obrazek
        names = ['happy.png','normal.png','sad.png']
        self.image = QLabel(self)
        self.pixmap = QPixmap(names[0])
        self.image.setPixmap(self.pixmap)
        self.image.setGeometry(140, 20, 140, 140)

        #progressbar
        self.progressBar = QProgressBar(self)
        self.progressBar.setOrientation(Qt.Vertical)
        self.progressBar.setValue(90)
        self.progressBar.setGeometry(140,180,40,160)
        self.label = QLabel('Wskaźnik zadowolenia',self)
        self.label.setGeometry(140, 350, 120, 20)

        #buttony
        self.button1 = QPushButton('OK', self)
        self.button1.move(370, 40)
        self.button1.clicked.connect(self.buttonClick)
        self.button2 = QPushButton('Anuluj', self)
        self.button2.move(370, 80)
        self.button2.clicked.connect(self.close)

        self.setGeometry(400, 400, 500, 400)
        self.setWindowTitle('Zmień ikonę')
        #print(self.setWinIcon())
        #self.show()

    @property
    def setWinIcon(self):
        return str(self.buttonGroup2.checkedId())

    @setWinIcon.getter
    def setWinIcon(self):
        #self.main = MainWindow()
        """
        buttonID = str(self.buttonGroup2.checkedId())
        if buttonID == '-2':
            self.icon = QIcon('happy.png')
            self.setWindowIcon(self.icon)
            #self.main.setWindowIcon(self.icon)
        elif buttonID == '-3':
            self.icon = QIcon('normal.png')
            self.setWindowIcon(self.icon)
            #self.main.setWindowIcon(self.icon)
        elif buttonID == '-4':
            self.icon = QIcon('sad.png')
            self.setWindowIcon(self.icon)
            #self.main.setWindowIcon(self.icon)
        print(buttonID)
        """
        return str(self.buttonGroup2.checkedId())

    def buttonClick(self):
        #if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
        self.changed.emit(self.setWinIcon)
        self.close()

    def image1(self):
        self.pixmap = QPixmap('happy.png')
        self.image.setPixmap(self.pixmap)
        self.image.setGeometry(140, 20, 140, 140)
        self.progressBar.setValue(100)
        self.checkbox1.setChecked(True)

    def image2(self):
        self.pixmap = QPixmap('normal.png')
        self.image.setPixmap(self.pixmap)
        self.image.setGeometry(140, 20, 140, 140)
        self.progressBar.setValue(50)
        self.checkbox2.setChecked(True)

    def image3(self):
        self.pixmap = QPixmap('sad.png')
        self.image.setPixmap(self.pixmap)
        self.image.setGeometry(140, 20, 140, 140)
        self.progressBar.setValue(10)
        self.checkbox3.setChecked(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = ChangeIcon()
    sys.exit(app.exec_())



