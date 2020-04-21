import PySide2, sys, psycopg2, dbconn, login
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QAction, QDateEdit, QHBoxLayout, QHeaderView, QLabel, QLineEdit, QMainWindow, QMessageBox, QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem, QWidget
from acquisto_ins import AcquistoForm
from prenotaz_ins import PrenotazioneForm
from ordine_ins import OrdineForm
from tablewidget import TableWidget
from querywidget import QueryWidget
from cliente_ins import ClienteForm

# Label : non-modal dialog class
INSERTIONS = {
    'Registrazione Acquisto': AcquistoForm,
    'Registrazione Prenotazione': PrenotazioneForm,
    'Registrazione Ordine' : OrdineForm,
    'Registrazione Cliente' : ClienteForm
}

# QUERIES = {Label : (function-name, {params-dict})}
# params-dict = {param-name : widget}
QUERIES = {
    'Bilancio': ('bilancio', ('Anno: ', QSpinBox)),
    'Editori con vendite per giorno': ('case_editrici_vendite', ('Data: ', QDateEdit)),
    'Dipendente più attivo' : ('dipendente_max_vendite', tuple()),
    'Fornitore più economico libro' : ('fornitore_min_prezzo', ('Libro: ', QLineEdit)),
    'Genere più venduto' : ('genere_max_venduto', tuple()),
    'Generi per autore' : ('generi_autore', ('Autore: ', QSpinBox)),
    'Generi per collana' : ('generi_collana', ('Collana: ', QLineEdit)),
    'Libri per genere' : ('libri_genere', ('Genere: ', QLineEdit))
}

GET_TABLES_QUERY = 'SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname NOT IN (\'pg_catalog\', \'information_schema\');'
GET_VIEWS_QUERY = 'SELECT viewname FROM pg_catalog.pg_views WHERE schemaname NOT IN (\'pg_catalog\',\'information_schema\');'
GET_ALL_FROM_X = 'SELECT * FROM {};'


class DbMainWindow(QMainWindow):

    def __init__(self, connection):
        '''
        Main window for the program, handles the basic table/view queries
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
            action = QAction(' '.join([t.capitalize() for t in table.replace('_', ' ').split()]), self)
            callback = self._make_show_table(table)
            action.triggered.connect(callback)
            self.table_menu.addAction(action)

        self.view_menu = self.menu.addMenu('Viste')
        for view in self.view_list:
            action = QAction(' '.join([v.capitalize() for v in view.replace('_', ' ').split()]), self)
            callback = self._make_show_table(view)
            action.triggered.connect(callback)
            self.view_menu.addAction(action)

        self.query_menu = self.menu.addMenu('Interrogazioni')
        for label, info in QUERIES.items():
            action = QAction(label, self)
            callback = self._make_show_query(info)
            action.triggered.connect(callback)
            self.query_menu.addAction(action)

        self.insert_menu = self.menu.addMenu('Inserimenti')
        for label, dialogclass in INSERTIONS.items():
            action = QAction(label, self)
            callback = self._make_show_dialog(dialogclass)
            action.triggered.connect(callback)
            self.insert_menu.addAction(action)

        self.connection.commit()

        # GUI init
        self.setWindowTitle('DbApp')
        self.table_widget = TableWidget()
        self.setCentralWidget(self.table_widget)

    def _make_show_table(self, table):
        def show_table():
            '''
            Display the content of a table in the main table view

            Parameters:
            table : str -- The table name to show, will be directly inserted in the query
            '''
            self.cursor.execute(GET_ALL_FROM_X.format(table))
            labels = [item[0] for item in self.cursor.description]
            self.table_widget = TableWidget()
            self.setCentralWidget(self.table_widget)
            self.table_widget.populate(labels, self.cursor.fetchall())
            self.connection.commit()
        return show_table
    
    def _make_show_query(self, info):
        def show_query():
            self.query_widget = QueryWidget(info, self.connection)
            self.setCentralWidget(self.query_widget)
        return show_query

    def _make_show_dialog(self, dialogclass):
        def show_dialog():
            self.last_dialog = dialogclass(self.connection)
            self.last_dialog.show()
        return show_dialog

    def _show_error(self, msg=''):
        dialog = QMessageBox()
        dialog.setWindowTitle('ERRORE')
        dialog.setText(msg)
        dialog.exec_()


def display_app(application, connection):

    widget = DbMainWindow(connection)
    widget.setWindowTitle('Gestore Libreria')
    widget.resize(960, 720)
    widget.show()

    return application.exec_()


if __name__ == '__main__':
    application = QtWidgets.QApplication([])
    ssh, params = login.show_dialog()
    if ssh:
        tunnel, conn = dbconn.connect_to_dei_ssh(**params)
        result = display_app(application, conn)
        conn.close()
        tunnel.close()
    else:
        conn = dbconn.connect_generic(**params)
        result = display_app(application, conn)
        conn.close()
    sys.exit(result)
