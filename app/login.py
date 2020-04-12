import sys
import dbconn
from PySide2.QtWidgets import QApplication, QDialog, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStackedLayout, QVBoxLayout
from PySide2 import QtCore


class GenericForm(QDialog):
    '''
    Shows a dialog with the interface for login. When the Login button is pressed, the values of the fields
    are set in the result dict and self.accept() is called. If the "Change mode" button is pressed then
    self.reject() is called.
    '''

    def __init__(self, result: dict, parent=None):
        '''
        Constructor.

        Parameters:
        result : dict -- The dictionary that will contain the values of the various fields, the constants in dbconn are used as keys.
        parent -- The parent app if any.
        '''
        super(GenericForm, self).__init__(parent)
        self.setWindowTitle('Login Locale')
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.result = result

        # Widgets for generic layout
        self.generics_w = {
            dbconn.PASSWORD: QLineEdit(),
            dbconn.HOST: QLineEdit('localhost'),
            dbconn.DATABASE: QLineEdit('postgres'),
            dbconn.USER: QLineEdit('postgres'),
            dbconn.PORT: QLineEdit('5433')
        }
        self.generics_w[dbconn.PASSWORD].setEchoMode(QLineEdit.Password)

        # Form layout
        self.generic_layout = QFormLayout()
        self.generic_layout.setRowWrapPolicy(QFormLayout.WrapLongRows)

        for k, v in self.generics_w.items():
            self.generic_layout.addRow(QLabel(k), v)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        self.change_button = QPushButton('SSH')
        self.change_button.clicked.connect(self.change)
        self.generic_layout.addRow(self.login_button, self.change_button)

        self.setLayout(self.generic_layout)

    # Returns the login credentials
    def login(self):
        print('Logging in...')
        for k, v in self.generics_w.items():
            self.result[k] = v.text()
        self.accept()

    # Rejects to signal that the mode should be changed
    def change(self):
        print('Changing mode...')
        self.reject()


class SshForm(QDialog):
    '''
    Shows a dialog with the interface for login. When the Login button is pressed, the values of the fields
    are set in the result dict and self.accept() is called. If the "Change mode" button is pressed then
    self.reject() is called.
    '''

    def __init__(self, result: dict, parent=None):
        '''
        Constructor.

        Parameters:
        result : dict -- The dictionary that will contain the values of the various fields, the constants in dbconn are used as keys.
        parent -- The parent app if any.
        '''
        super(SshForm, self).__init__(parent)
        self.setWindowTitle('Login Dbstud (SSH)')
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.result = result
        # Widgets for ssh layout
        self.ssh_w = {
            dbconn.SSH_USER: QLineEdit(),
            dbconn.SSH_PASSWORD: QLineEdit(),
            dbconn.SSH_DATABASE: QLineEdit(),
            dbconn.USER_PASSWORD: QLineEdit()
        }
        self.ssh_w[dbconn.SSH_PASSWORD].setEchoMode(QLineEdit.Password)
        self.ssh_w[dbconn.USER_PASSWORD].setEchoMode(QLineEdit.Password)

        # Form Layout
        self.ssh_layout = QFormLayout()
        self.ssh_layout.setRowWrapPolicy(QFormLayout.WrapLongRows)

        for k, v in self.ssh_w.items():
            self.ssh_layout.addRow(QLabel(k), v)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        self.change_button = QPushButton('Locale')
        self.change_button.clicked.connect(self.change)
        self.ssh_layout.addRow(self.login_button, self.change_button)

        # Add button signal for login
        self.setLayout(self.ssh_layout)

    # Greets the user
    def login(self):
        print('Logging in...')
        for k, v in self.ssh_w.items():
            self.result[k] = v.text()
        self.accept()

    # Rejects to signal that the mode should be changed
    def change(self):
        print('Changing mode...')
        self.reject()


def show_dialog():
    '''
    Function showing the dialogs. Must be called from inside a QApplication

    Returns:
    ssh : boolean -- Whether the connection should be via ssh or to the local db
    result : dict -- The params for the connections, can be directly fed into dbconn.py
    '''
    # Create and show the form
    result = {}
    form = GenericForm(result=result)
    form.show()
    show_ssh = True
    # Run the main Qt loop
    while form.exec_() != QDialog.Accepted:
        if show_ssh:
            form = SshForm(result=result)
        else:
            form = GenericForm(result=result)
        show_ssh = not show_ssh
        form.show()
    return (not show_ssh), result