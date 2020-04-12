import PySide2
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QAction, QDialog, QApplication, QDateEdit, QDoubleSpinBox, QErrorMessage, QFormLayout, QHBoxLayout, QHeaderView, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sys
import psycopg2
from PySide2.QtCore import QDate
import re

# See column names
INSERT_CLIENTE = 'INSERT INTO cliente (nome, cognome, data_nascita, telefono, email) VALUES (%s, %s, %s, %s, %s);'


class ClienteForm(QDialog):
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
        self.setWindowTitle('Aggiungi Cliente')
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.conn = conn
        self.cursor = conn.cursor()

        self.gen_layout = QVBoxLayout()

        self.form_layout = QFormLayout()
        self.form_layout.setRowWrapPolicy(QFormLayout.WrapLongRows)

        # Widgets

        self.nome_field = QLineEdit()
        self.form_layout.addRow('Nome: ', self.nome_field)

        self.cognome_field = QLineEdit()
        self.form_layout.addRow('Cognome: ', self.cognome_field)

        self.date_field = QDateEdit(QDate.currentDate())
        self.date_field.setDisplayFormat("MM/dd/yyyy")
        self.date_field.setCalendarPopup(True)
        self.form_layout.addRow(
            'Data di nascita (mm/gg/aaaa): ', self.date_field)

        self.phone_field = QLineEdit()
        self.form_layout.addRow('Telefono (solo cifre): ', self.phone_field)

        self.email_field = QLineEdit()
        self.form_layout.addRow('E-Mail: ', self.email_field)

        self.confirm_button = QPushButton('Conferma')
        self.confirm_button.clicked.connect(self.post_cliente)

        self.gen_layout.addLayout(self.form_layout)
        self.gen_layout.addWidget(self.confirm_button)
        self.setLayout(self.gen_layout)

    def verif_data(self):
        if not self.nome_field.text().strip():
            self._show_error('Il nome non può essere vuoto.')
            return False
        if not self.cognome_field.text().strip():
            self._show_error('Il cognome non può essere vuoto.')
            return False
        phone = self.phone_field.text().strip()
        email = self.email_field.text().strip()
        if not phone and not email:
            self._show_error(
                'Almeno uno fra telefono ed e-mail deve essere non vuoto.')
            return False
        if phone and not re.match('[0-9]{3,15}', phone):
            self._show_error('Numero di telefono non valido.')
            return False
        if email and not re.match('[A-Za-z0-9\.]{1,}@[A-Za-z0-9\.]{1,}', email):
            self._show_error('E-Mail non valida.')
            return False
        return True

    def post_cliente(self):

        if not self.verif_data():
            return

        nome = self.nome_field.text().strip()
        cognome = self.cognome_field.text().strip()
        data = self.date_field.date().toString('MM/dd/yyyy')
        phone = self.phone_field.text().strip()
        email = self.email_field.text().strip()

        self.cursor.execute(INSERT_CLIENTE, (
            nome,
            cognome,
            data,
            phone,
            email
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

    widget = ClienteForm(conn)
    widget.resize(850, 480)
    widget.show()

    sys.exit(application.exec_())
