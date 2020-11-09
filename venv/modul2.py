from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5.QtCore import Qt , pyqtSignal
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QObject

import sys

class CustomDialog2(QDialog):
    changed2 = pyqtSignal(int)
    def __init__(self, *args,parent=None, title=''):
        super(CustomDialog2, self).__init__()
        self.setWindowTitle("Ustaw koła")
        #qp = QPainter()
        #d1 = MainWindow.drawRectangles(self,qp, index)
        #self.slider1.setValue(d1[0])

        #self.setSilders(d1[0],d1[1])
        self.setSilders(200, 100)

        #widget layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        #self.setGeometry(300, 300, 500, 200)
        self.setFixedSize(500, 200)
        #self.show()


    def valueChangedSilder(self):
        txt1 = str(self.slider1.value())
        self.field1.setText(txt1)
        txt2 = str(self.slider2.value())
        self.field2.setText(txt2)

    def valueChangedField1(self):
        self.text1 = self.field1.text()
        self.slider1.setValue(int(self.text1))
        #return self.text1

    def valueChangedField2(self):
        self.text2 = self.field2.text()
        self.slider2.setValue(int(self.text2))
        #return text2

    def setSilders(self,s1, s2):
        # labelki
        self.label1 = QLabel("Na zewnątrz", self)
        self.label1.move(20, 20)
        self.label2 = QLabel("Wewnątrz", self)
        self.label2.move(20, 60)

        # pola edycyjne
        self.field1 = QLineEdit(self)
        self.field1.move(210, 25)
        self.field1.resize(30, 20)
        self.field2 = QLineEdit(self)
        self.field2.move(210, 65)
        self.field2.resize(30, 20)

        # slidery
        self.slider1 = QSlider(Qt.Horizontal, self)
        self.slider1.setMinimum(1)
        self.slider1.setMaximum(400)
        self.slider1.move(100, 20)
        self.slider1.setValue(s1)
        self.slider1.valueChanged.connect(self.valueChangedSilder)
        self.field1.textChanged.connect(self.valueChangedField1)
        self.slider2 = QSlider(Qt.Horizontal, self)
        self.slider2.setMinimum(1)
        self.slider2.setMaximum(400)
        self.slider2.move(100, 60)
        self.slider2.setValue(s2)
        self.slider2.valueChanged.connect(self.valueChangedSilder)
        self.field2.textChanged.connect(self.valueChangedField2)
        self.valueChangedSilder()

        # przyciski
        self.button1 = QPushButton('Anuluj', self)
        self.button1.move(370, 140)
        self.button1.clicked.connect(self.close)
        self.button2 = QPushButton('OK', self)
        self.button2.move(250, 140)
        self.button2.clicked.connect(self.buttonClick)

    @property
    def getSlidersValue(self):
        return self.slider1.value()

    @getSlidersValue.getter
    def getSlidersValue(self):
        self.s1 = self.slider1.value()
        self.s2 = self.slider2.value()
        print(self.s1,self.s2)
        self.close()
        return int(self.slider1.value())

    def buttonClick(self):
        #if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
        self.changed2.emit(self.getSlidersValue)
        self.close()


def main():
    app = QApplication(sys.argv)
    dialog = CustomDialog2()
    sys.exit(app.exec_())

if __name__ == '__main__':
  main()