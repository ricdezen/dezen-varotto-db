import PySide2
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QAction, QHeaderView, QMainWindow, QTableWidget, QTableWidgetItem, QWidget
import sys
import psycopg2
import dbconn
import login

GET_TABLES_QUERY = 'SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname NOT IN (\'pg_catalog\', \'information_schema\');'
GET_VIEWS_QUERY = 'SELECT viewname FROM pg_catalog.pg_views WHERE schemaname NOT IN (\'pg_catalog\',\'information_schema\');'
GET_ALL_FROM_X = 'SELECT * FROM {};'


class TableWidget(QWidget):

    def __init__(self):
        '''
        # TODO
        '''
        super().__init__()

        # Table
        self.table = QTableWidget()
        self.item_count = 0

        # Layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def populate(self, labels: list, values: list):
        '''
        Method used to populate the table with the results of a query
        Parameters:
        labels : list -- The list of labels.
        values : list -- A list of tuples containing the values to display. len(values[i]) = len(labels) for each i
        '''
        self.table.clear()
        while self.table.rowCount() > 0 :
            self.table.removeRow(0)
        self.item_count = 0
        self.table.setColumnCount(len(labels))
        self.table.setHorizontalHeaderLabels(labels)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for row in values :
            self.table.insertRow(self.item_count)
            for i in range(len(labels)):
                self.table.setItem(self.item_count, i, QTableWidgetItem(str(row[i])))
            self.item_count += 1


class DbMainWindow(QMainWindow):

    def __init__(self, connection):
        '''
        #TODO
        '''
        super().__init__()
        # Param refs
        self.connection = connection
        self.cursor = self.connection.cursor()

        # Get db meta
        self.cursor.execute(GET_TABLES_QUERY)
        self.table_list = [item[0] for item in self.cursor.fetchall()]
        self.cursor.execute(GET_VIEWS_QUERY)
        self.view_list = [item[0] for item in self.cursor.fetchall()]

        # Menu init
        self.menu = self.menuBar()
        self.table_menu = self.menu.addMenu('Tabelle')
        for table in self.table_list:
            action = QAction(table, self)
            callback = self.__make_show_table(table)
            action.triggered.connect(callback)
            self.table_menu.addAction(action)
        self.view_menu = self.menu.addMenu('Viste')
        for view in self.view_list:
            action = QAction(view, self)
            callback = self.__make_show_table(view)
            action.triggered.connect(callback)
            self.view_menu.addAction(action)

        self.connection.commit()

        # GUI init
        self.setWindowTitle('DbApp')
        self.table_widget = TableWidget()
        self.setCentralWidget(self.table_widget)

    def __make_show_table(self, table):
        def show_table():
            '''
            Display the content of a table in the main table view

            Parameters:
            table : str -- The table name to show, will be directly inserted in the query
            '''
            print(table)
            self.cursor.execute(GET_ALL_FROM_X.format(table))
            labels = [item[0] for item in self.cursor.description]
            print(labels)
            self.table_widget.populate(labels, self.cursor.fetchall())
            self.connection.commit()
        return show_table

    def __show_error(self, error: int):
        '''
        # TODO
        '''
        pass


def display_app(application, connection):

    widget = DbMainWindow(connection)
    widget.resize(1280, 720)
    widget.show()

    return application.exec_()


if __name__ == '__main__':
    application = QtWidgets.QApplication([])
    # TODO hide password
    ssh, params = login.show_dialog()
    if ssh :
        tunnel, conn = dbconn.connect_to_dei_ssh(**params)
        result = display_app(application, conn)
        conn.close()
        tunnel.close()
    else :
        conn = dbconn.connect_generic(**params)
        result = display_app(application, conn)
        conn.close()
    sys.exit(result)
