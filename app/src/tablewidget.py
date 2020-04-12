from PySide2.QtWidgets import QWidget, QHBoxLayout, QHeaderView, QLabel, QLineEdit, QSizePolicy, QTableWidget, QTableWidgetItem
from PySide2 import QtWidgets

class TableWidget(QWidget):

    def __init__(self):
        '''
        # TODO
        '''
        super().__init__()

        # Data
        self.values = []
        self.values_view = []
        self.labels = []

        # Search bar
        self.search_label = QLabel('Cerca')
        self.search_bar = QLineEdit()
        self.search_bar.setSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.search_bar.textChanged[str].connect(self.update_table)
        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(self.search_label)
        self.search_layout.addWidget(self.search_bar)

        # Table
        self.table = QTableWidget()
        self.item_count = 0

        # Layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.search_layout)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def populate(self, labels: list, values: list):
        '''
        Method used to populate the table with the results of a query
        Parameters:
        labels : list -- The list of labels.
        values : list -- A list of tuples containing the values to display. len(values[i]) = len(labels) for each i
        '''
        self.labels = labels
        self.values = values
        self.update_table()

    def update_table(self):
        '''
        Updates the table by filtering the rows and reloading the table
        '''
        self.filter_rows()
        self.load_table()

    def load_table(self):
        self.table.clear()
        while self.table.rowCount() > 0:
            self.table.removeRow(0)
        self.item_count = 0
        self.table.setColumnCount(len(self.labels))
        self.table.setHorizontalHeaderLabels(self.labels)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for row in self.values_view:
            self.table.insertRow(self.item_count)
            for i in range(len(self.labels)):
                self.table.setItem(self.item_count, i,
                                   QTableWidgetItem(str(row[i])))
            self.item_count += 1

    def filter_rows(self):
        '''
        Filters the data to display based on the string in self.search_bar
        '''
        self.values_view = []
        for row in self.values:
            if self.search_bar.text().lower() in str(row).lower():
                self.values_view.append(row)