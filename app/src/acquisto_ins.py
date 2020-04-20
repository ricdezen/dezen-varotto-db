import PySide2
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QAction, QDialog, QApplication, QDateEdit, QDoubleSpinBox, QErrorMessage, QFormLayout, QHBoxLayout, QHeaderView, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sys
import psycopg2
from PySide2.QtCore import QDate

# id
FIND_CLIENTE = 'SELECT id FROM cliente WHERE id = %s;'
# cf
FIND_DIPENDENTE = 'SELECT cf FROM dipendente WHERE cf = %s;'
# isbn
FIND_QUANTITA = 'SELECT disponibili FROM libro WHERE isbn = %s;'
# date, money, dipendente
INSERT_ACQUISTO = 'INSERT INTO acquisto (data_acquisto, importo, dipendente) VALUES (%s, %s, %s) RETURNING numero;'
# num, cliente
INSERT_IMMEDIATO = 'INSERT INTO a_immediato (numero, cliente) VALUES (%s, %s);'
# num, book, qty
INSERT_COMPRENDE = 'INSERT INTO comprende (acquisto, libro, quantita) VALUES (%s, %s, %s);'
# isbn, qty_to_subtract, isbn
DECREASE_LIBRO = 'UPDATE libro SET disponibili = ((SELECT disponibili FROM libro WHERE isbn = %s) - %s) WHERE isbn = %s;'


class AcquistoForm(QDialog):
    '''
    Widget per l'inserimento di un acquisto immediato.
    '''

    def __init__(self, conn):
        '''
        Parameters:
            conn : connection
                Connection to the database.
        '''
        super().__init__()
        self.setWindowTitle('Aggiungi Acquisto')
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.conn = conn
        self.cursor = conn.cursor()

        self.books = dict()
        self.books_qt = dict()

        self.gen_layout = QVBoxLayout()

        self.form_layout = QFormLayout()
        self.form_layout.setRowWrapPolicy(QFormLayout.WrapLongRows)

        # Widgets
        self.client_field = QLineEdit()
        self.form_layout.addRow(
            'Numero Cliente (facoltativo): ', self.client_field)

        self.dip_field = QLineEdit()
        self.form_layout.addRow('Dipendente (CF): ', self.dip_field)

        self.date_picker = QDateEdit(QDate.currentDate())
        self.date_picker.setDisplayFormat("MM/dd/yyyy")
        self.date_picker.setCalendarPopup(True)
        self.form_layout.addRow('Data (mm/gg/aaaa): ', self.date_picker)

        self.importo_field = QDoubleSpinBox()
        self.importo_field.setMaximum(999999999.99)
        self.form_layout.addRow('Importo: ', self.importo_field)

        self.ins_layout = QHBoxLayout()
        self.libro_field = QLineEdit()
        self.quantita_field = QSpinBox()
        self.quantita_field.setMinimum(1)
        self.libro_button = QPushButton('Aggiungi')
        self.libro_button.clicked.connect(self.aggiungi_libro)
        self.ins_layout.addWidget(QLabel('Libro (ISBN): '))
        self.ins_layout.addWidget(self.libro_field)
        self.ins_layout.addWidget(QLabel('Quantità: '))
        self.ins_layout.addWidget(self.quantita_field)
        self.ins_layout.addWidget(self.libro_button)

        self.labels = ['ISBN', 'Quantità', '']
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(self.labels)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(
            2, QHeaderView.ResizeToContents)

        self.confirm_button = QPushButton('Conferma')
        self.confirm_button.clicked.connect(self.post_acquisto)

        self.gen_layout.addLayout(self.form_layout)
        self.gen_layout.addLayout(self.ins_layout)
        self.gen_layout.addWidget(self.table)
        self.gen_layout.addWidget(self.confirm_button)
        self.setLayout(self.gen_layout)

    def aggiungi_libro(self):
        self.books[self.libro_field.text()] = self.quantita_field.value()
        self.update_table()

    def remove_libro(self, book):
        self.books.pop(book, None)
        self.update_table()

    def update_table(self):
        self.table.clearContents()
        while self.table.rowCount() > 0:
            self.table.removeRow(0)
        for book in self.books.keys():
            row = self.table.rowCount()
            button = QPushButton('Rimuovi')
            button.clicked.connect(lambda: self.remove_libro(book))
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(book))
            self.table.setItem(row, 1, QTableWidgetItem(str(self.books[book])))
            self.table.setCellWidget(row, 2, button)

    def verif_money(self):
        if not self.importo_field.value():
            self._show_error('Importo pari a 0')
            return 1
        return 0

    def verif_qty(self):
        '''
        Shows error messages based on the validity of inserted books, and
        returns False, or returns True if all the books are ok to sell right now.
        '''
        if len(self.books.items()) == 0:
            self._show_error('Non ci sono libri nell\'acquisto')
            return 1
        for book, qty in self.books.items():
            self.cursor.execute(FIND_QUANTITA, (book,))
            result = self.cursor.fetchall()
            if not result:
                self._show_error('\'{}\' non è un libro valido.'.format(book))
                return 2
            stored = result[0][0]
            if stored < qty:
                return self.__show_are_you_sure(
                    'L\'acquisto richiede {} libri {}, ma ne sono presenti solo {}. Non sarà possibile sottrarre i libri, vuoi proseguire ugualmente?'.format(qty, book, stored))
        return 0

    def verif_client_dip(self):
        '''
        Returns false and displays and error message if cliente and dipendente are
        not valid tuples in the database, returns true if they are ok
        '''
        cliente = self.client_field.text()
        if cliente:
            if not cliente.isdigit():
                self._show_error('Il codice del Cliente deve essere numerico.')
                return 1
            self.cursor.execute(FIND_CLIENTE, (cliente,))
            result = self.cursor.fetchall()
            if not result or not result[0][0]:
                self._show_error('Cliente {} non esiste.'.format(cliente))
                return 2

        dipendente = self.dip_field.text()
        if not dipendente:
            self._show_error('Il Dipendente non può essere vuoto.')
            return 3
        self.cursor.execute(FIND_DIPENDENTE, (dipendente,))
        result = self.cursor.fetchall()
        if not result or not result[0][0]:
            self._show_error('Dipendente {} non esiste.'.format(dipendente))
            return 4
        return 0

    def post_acquisto(self):
        if self.verif_money():
            return
        if self.verif_client_dip():
            return
        should_show = self.verif_qty()
        if should_show > 0:
            return
        cliente = self.client_field.text().strip(
        ) if self.client_field.text().strip() else None
        importo = self.importo_field.value()
        self.cursor.execute(INSERT_ACQUISTO, (
            self.date_picker.date().toString('MM/dd/yyyy'),
            self.importo_field.value(),
            self.dip_field.text()
        ))
        new_id = self.cursor.fetchall()[0][0]
        self.cursor.execute(INSERT_IMMEDIATO, (new_id, cliente))
        for book in self.books.keys():
            self.cursor.execute(
                INSERT_COMPRENDE, (new_id, book, self.books[book]))
        self.conn.commit()
        if should_show == 0 : self._show_confirm()
        self.accept()

    def __show_are_you_sure(self, msg=''):
        dialog = _AreYouSureDialog(msg)
        dialog.setWindowTitle('ATTENZIONE')
        result = dialog.exec_()
        return -1 if result == QDialog.Accepted else 3

    def _show_confirm(self):
        dialog = _ScalaAcquistiDialog(self.books, self.conn)
        dialog.setWindowTitle('Rimozione libri')
        dialog.exec_()

    def _show_error(self, msg=''):
        dialog = QMessageBox()
        dialog.setWindowTitle('ERRORE')
        dialog.setText(msg)
        dialog.exec_()


class _AreYouSureDialog(QDialog):
    def __init__(self, msg):
        super().__init__()

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.message_label = QLabel(msg)

        self.yes_btn = QPushButton('Sì')
        self.yes_btn.clicked.connect(self.accept)

        self.no_btn = QPushButton('No')
        self.no_btn.clicked.connect(self.reject)

        self.bot_buttons = QHBoxLayout()
        self.bot_buttons.addWidget(self.yes_btn)
        self.bot_buttons.addWidget(self.no_btn)

        self.gen_layout = QVBoxLayout()
        self.gen_layout.addWidget(self.message_label)
        self.gen_layout.addLayout(self.bot_buttons)

        self.setLayout(self.gen_layout)


class _ScalaAcquistiDialog(QDialog):
    def __init__(self, books: dict, conn):
        super().__init__()
        self.conn = conn
        self.cursor = conn.cursor()
        self.books = books

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.header_text = QLabel(
            'Vuoi sottrarre al database i libri dell\'acquisto?')
        self.body_text = QLabel(self._make_body())

        self.yes_btn = QPushButton('Sì')
        self.yes_btn.clicked.connect(self._decrease_books)

        self.no_btn = QPushButton('No')
        self.no_btn.clicked.connect(self.reject)

        self.bot_buttons = QHBoxLayout()
        self.bot_buttons.addWidget(self.yes_btn)
        self.bot_buttons.addWidget(self.no_btn)

        self.gen_layout = QVBoxLayout()
        self.gen_layout.addWidget(self.header_text)
        self.gen_layout.addWidget(self.body_text)
        self.gen_layout.addLayout(self.bot_buttons)

        self.setLayout(self.gen_layout)

    def _make_body(self):
        return '\n'.join(['{} x {}'.format(k, v) for k, v in self.books.items()])

    def _decrease_books(self):
        for book, qty in self.books.items():
            self.cursor.execute(DECREASE_LIBRO, (book, qty, book))
        self.conn.commit()
        self.accept()


if __name__ == '__main__':
    application = QtWidgets.QApplication([])

    pwd = input('Password: ')
    conn = psycopg2.connect(database='postgres',
                            user='postgres', password=pwd, port=5433)

    widget = AcquistoForm(conn)
    widget.resize(960, 720)
    widget.show()

    sys.exit(application.exec_())
