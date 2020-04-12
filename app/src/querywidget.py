import PySide2
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QAction, QDateEdit, QHBoxLayout, QHeaderView, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sys
import psycopg2
from tablewidget import TableWidget

class QueryWidget(QWidget):
    def __init__(self, info : tuple, conn):
        super().__init__()
        self.conn = conn
        self.cursor = conn.cursor()
        self.fun_name = info[0]
        self.param = info[1]
        self.labels = []
        self.values = []

        self.gen_layout = QVBoxLayout()

        self.table = TableWidget()
        self.input = None

        if self.param :
            self.label = QLabel(self.param[0])
            self.input = self.param[1]()
            if self.param[1] == QDateEdit :
                self.input.setDisplayFormat("MM/dd/yyyy")
                self.input.setCalendarPopup(True)
            if self.param[1] == QSpinBox :
                self.input.setMaximum(999999999999999)
            self.button = QPushButton('Esegui')
            self.button.clicked.connect(self._run_query)
            self.row = QHBoxLayout()
            self.row.addWidget(self.label)
            self.row.addWidget(self.input)
            self.row.addWidget(self.button)
            self.gen_layout.addLayout(self.row)
        
        self.gen_layout.addWidget(self.table)

        self.setLayout(self.gen_layout)
        if not self.param : self._run_query()
    
    def _get_param(self):
        if not self.input : return None
        if type(self.input) == QDateEdit : return self.input.date().toString('MM/dd/yyyy')
        if type(self.input) == QLineEdit : return self.input.text()
        if type(self.input) == QSpinBox : return self.input.value()
        return None

    def _run_query(self):
        param = self._get_param()
        if param :
            self.cursor.callproc(self.fun_name, (self._get_param(),))
        else :
            self.cursor.callproc(self.fun_name)
        labels = [item[0] for item in self.cursor.description]
        self.table.populate(labels, self.cursor.fetchall())
        self.conn.commit()