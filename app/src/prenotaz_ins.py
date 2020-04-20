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
# date, money, dipendente
INSERT_ACQUISTO = 'INSERT INTO acquisto (data_acquisto, importo, dipendente) VALUES (%s, %s, %s) RETURNING numero;'
# num, book, qty
INSERT_COMPRENDE = 'INSERT INTO comprende (acquisto, libro, quantita) VALUES (%s, %s, %s);'
# num, cliente
INSERT_PRENOTAZIONE = 'INSERT INTO prenotazione (numero, cliente, stato) VALUES (%s, %s, \'Transito\');'


class PrenotazioneForm(QDialog):
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
        self.setWindowTitle('Aggiungi Prenotazione')
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
        self.form_layout.addRow('Numero Cliente: ', self.client_field)

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

        self.info_label = QLabel(
            'Le prenotazioni non riducono i libri disponibili.')
        self.confirm_button = QPushButton('Conferma')
        self.confirm_button.clicked.connect(self.post_prenotazione)

        self.gen_layout.addLayout(self.form_layout)
        self.gen_layout.addLayout(self.ins_layout)
        self.gen_layout.addWidget(self.table)
        self.gen_layout.addWidget(self.info_label)
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

    def verif_libri(self):
        '''
        Shows error messages based on the validity of inserted books, and
        returns False, or returns True if all the books are ok to sell right now.
        '''
        if len(self.books.items()) == 0:
            self._show_error('Non ci sono libri nell\'acquisto')
            return False
        for book in self.books.keys():
            self.cursor.execute('SELECT * FROM libro WHERE isbn = %s', (book,))
            result = self.cursor.fetchall()
            if not result:
                self._show_error('\'{}\' non è un libro valido.'.format(book))
                return False
        return True

    def verif_client_dip(self):
        '''
        Returns false and displays and error message if cliente and dipendente are
        not valid tuples in the database, returns true if they are ok
        '''
        cliente = self.client_field.text()
        if not cliente:
            self._show_error('Il Cliente è necessario per una Prenotazione.')
            return False
        if cliente:
            if not cliente.isdigit():
                self._show_error('Il codice del Cliente deve essere numerico.')
                return False
            self.cursor.execute(FIND_CLIENTE, (cliente,))
            result = self.cursor.fetchall()
            if not result or not result[0][0]:
                self._show_error('Cliente {} non esiste.'.format(cliente))
                return False

        dipendente = self.dip_field.text()
        if not dipendente:
            self._show_error('Il Dipendente non può essere vuoto.')
            return False
        self.cursor.execute(FIND_DIPENDENTE, (dipendente,))
        result = self.cursor.fetchall()
        if not result or not result[0][0]:
            self._show_error('Dipendente {} non esiste.'.format(dipendente))
            return False
        return True

    def post_prenotazione(self):
        if not self.verif_libri():
            return
        if not self.verif_client_dip():
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
        self.cursor.execute(INSERT_PRENOTAZIONE, (new_id, cliente))
        for book in self.books.keys():
            self.cursor.execute(
                INSERT_COMPRENDE, (new_id, book, self.books[book]))
        self.conn.commit()
        self._show_confirm()
        self.accept()

    def _show_confirm(self):
        dialog = QMessageBox()
        dialog.setWindowTitle('Conferma Prenotazione')
        msg = 'Registrato prenotazione per i seguenti libri:\n{}'
        dialog.setText(
            msg.format('\n'.join(['{} x {}'.format(k, v)
                                  for k, v in self.books.items()]))
        )
        dialog.exec_()

    def _show_error(self, msg=''):
        dialog = QMessageBox()
        dialog.setWindowTitle('ERRORE')
        dialog.setText(msg)
        dialog.exec_()

if __name__ == '__main__':
    application = QtWidgets.QApplication([])

    pwd = input('Password: ')
    conn = psycopg2.connect(database='postgres',
                            user='postgres', password=pwd, port=5433)

    widget = PrenotazioneForm(conn)
    widget.resize(960, 720)
    widget.show()

    sys.exit(application.exec_())