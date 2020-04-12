import PySide2
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QAction, QDialog, QApplication, QDateEdit, QDoubleSpinBox, QErrorMessage, QFormLayout, QHBoxLayout, QHeaderView, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sys
import psycopg2
from PySide2.QtCore import QDate

# cf
FIND_DIPENDENTE = 'SELECT cf FROM dipendente WHERE cf = %s;'
# isbn
FIND_CATALOGO = 'SELECT libro FROM catalogo WHERE fornitore = %s;'
# See column names
INSERT_ORDINE = 'INSERT INTO ordine (dipendente, data_ordine, fornitore, libro, importo, quantita) VALUES (%s, %s, %s, %s, %s, %s);'


class OrdineForm(QDialog):
    '''
    Dialog per l'inserimento di un ordine.
    '''

    def __init__(self, conn):
        '''
        Parameters:
            conn : connection
                Connection to the database.
        '''
        super().__init__()
        self.setWindowTitle('Aggiungi Ordine')
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.conn = conn
        self.cursor = conn.cursor()

        self.gen_layout = QVBoxLayout()

        self.form_layout = QFormLayout()
        self.form_layout.setRowWrapPolicy(QFormLayout.WrapLongRows)

        # Widgets

        self.dip_field = QLineEdit()
        self.form_layout.addRow('Dipendente (CF): ', self.dip_field)

        self.date_picker = QDateEdit(QDate.currentDate())
        self.date_picker.setDisplayFormat("MM/dd/yyyy")
        self.date_picker.setCalendarPopup(True)
        self.form_layout.addRow('Data (mm/gg/aaaa): ', self.date_picker)

        self.forn_field = QLineEdit()
        self.form_layout.addRow('Fornitore (P.IVA): ', self.forn_field)

        self.libro_field = QLineEdit()
        self.form_layout.addRow('Libro (ISBN): ', self.libro_field)

        self.quant_field = QSpinBox()
        self.quant_field.setMinimum(1)
        self.quant_field.setMaximum(9999)
        self.form_layout.addRow('Quantità: ', self.quant_field)

        self.importo_field = QDoubleSpinBox()
        self.importo_field.setMaximum(999999999.99)
        self.form_layout.addRow('Importo: ', self.importo_field)

        self.confirm_button = QPushButton('Conferma')
        self.confirm_button.clicked.connect(self.post_ordine)

        self.gen_layout.addLayout(self.form_layout)
        self.gen_layout.addWidget(self.confirm_button)
        self.setLayout(self.gen_layout)

    def verif_money(self):
        if not self.importo_field.value():
            self._show_error('Importo pari a 0')
            return False
        return True

    def verif_dist(self):
        '''
        Checks that the fornitore is available and that the book is in its catalogue
        '''
        cursor = self.cursor
        forn = self.forn_field.text()
        book = self.libro_field.text()
        cursor.execute('SELECT piva FROM distributore;')
        available_forns = [x[0] for x in cursor.fetchall()]
        if forn not in available_forns:
            self._show_error('Il fornitore {} non esiste.'.format(forn))
            return False
        cursor.execute(FIND_CATALOGO, (forn,))
        available_books = [x[0] for x in cursor.fetchall()]
        if book not in available_books :
            self._show_error('Il libro {} non è nel catalogo del fornitore {}.'.format(book, forn))
        return book in available_books

    def verif_dip(self):
        '''
        Returns false and displays and error message if dipendente is
        not a valid tuple in the database, returns true if it is.
        '''
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

    def post_ordine(self):
        if not self.verif_money():
            return
        if not self.verif_dip():
            return
        if not self.verif_dist():
            return
        dipendente = self.dip_field.text()
        data_ordine = self.date_picker.date().toString('MM/dd/yyyy')
        fornitore = self.forn_field.text()
        libro = self.libro_field.text()
        importo = self.importo_field.value()
        quantita = self.quant_field.value()
        
        self.cursor.execute(INSERT_ORDINE, (
            dipendente,
            data_ordine,
            fornitore,
            libro,
            importo,
            quantita
        ))

        self.conn.commit()
        self.accept()

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

    widget = OrdineForm(conn)
    widget.resize(850, 480)
    widget.show()

    sys.exit(application.exec_())
