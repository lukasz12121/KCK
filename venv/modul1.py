from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QObject
import sys





class CustomDialog(QDialog):
    changed1 = pyqtSignal(int)
    def __init__(self, parent=None, title=''):
        super(CustomDialog, self).__init__()
        role = QtCore.Qt.BackgroundRole
        self.setWindowTitle("Ustaw kolor okna głównego")

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(':memory:')
        self.db.open()
        self.db.transaction()
        self.db.exec_(
            'CREATE TABLE partable'
            '(id INTEGER PRIMARY KEY, param TEXT NOT NULL)'
        )
        self.db.exec_("INSERT INTO partable VALUES(1, 'Czerwony')")
        self.db.exec_("INSERT INTO partable VALUES(2, 'Zielony')")
        self.db.exec_("INSERT INTO partable VALUES(3, 'Błękitny')")
        self.db.exec_("INSERT INTO partable VALUES(4, 'Żółty')")
        self.db.commit()
        """model = CustomSqlModel(self)"""

        model = QtSql.QSqlTableModel(self)
        #model = CustomSqlModel()
        model.setTable('partable')
        column = model.fieldIndex('param')
        model.select()
        self.combo = QComboBox(self)
        #self.combo.setEditable(False)
        self.combo.setModel(model)
        self.combo.setModelColumn(column)
        self.combo.activated.connect(self.comboClick)
        """self.combo.lineEdit().returnPressed.connect(self.handleComboEdit)"""

        layout = QVBoxLayout(self)
        layout.addWidget(self.combo)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 500, 50)
        #self.show()

    @property
    def passComboValue(self):
        return

    @passComboValue.getter
    def passComboValue(self):
        return self.combo.currentIndex()

    def comboClick(self):
        # if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
        self.changed1.emit(self.passComboValue)
        self.close()





class CustomSqlModel(QtSql.QSqlTableModel):
    """def __init__(self, parent=None):
        QtSql.QSqlTableModel.__init__(self, parent=parent)"""

    def data(self, index, role):
        if role == QtCore.Qt.BackgroundRole:
            if index.row() in [1]:
                return QtGui.QBrush(QtCore.Qt.red)
            elif index.row() in [2]:
                return QtGui.QBrush(QtCore.Qt.green)
            elif index.row() in [3]:
                return QtGui.QBrush(QtCore.Qt.blue)
            elif index.row() in [4]:
                return QtGui.QBrush(QtCore.Qt.yellow)
        return QtSql.QSqlTableModel.data(self, index, role)

def main():
     app = QApplication(sys.argv)
     dialog = CustomDialog()
     sys.exit(app.exec_())

if __name__ == '__main__':
  main()
