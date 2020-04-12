import sshtunnel
import psycopg2

# Keys to use when passing a dictionary to the method
SSH_USER = 'ssh_user'
SSH_PASSWORD = 'ssh_password'
SSH_DATABASE = 'database'
USER_PASSWORD = 'password'

def connect_to_dei_ssh(ssh_user: str, ssh_password: str, database: str, password: str):
    '''
    Method to connect to the Unipd DEI server via ssh

    Parameters:
    ssh_usr : str -- The username for the ssh connection
    ssh_pwd : str -- The password for the connection
    db_name : str -- The database name
    db_pwd : str -- The database password

    Returns:
    tunnel : The SSH tunnel, must be closed after use
    conn : The Connection, must be closed after use
    '''
    tunnel = sshtunnel.SSHTunnelForwarder(
        ('login.dei.unipd.it', 22),
        ssh_username=ssh_user,
        ssh_password=ssh_password,
        remote_bind_address=('dbstud.dei.unipd.it', 5432)
    )
    tunnel.start()

    return tunnel, connect_generic(password, database=database, user=ssh_user, port=tunnel.local_bind_port)

# Keys to use when passing a dictionary to the method
PASSWORD = 'password'
HOST = 'host'
DATABASE = 'database'
USER = 'user'
PORT = 'port'

def connect_generic(password, host='localhost', database='postgres', user='postgres', port=5433):
    '''
    Attempts to connect to the given database

    Parameters:
    host : str -- Database host, defaults to localhost
    database : str -- Database name, defaults to postgres
    user : str -- Username, defaults to postgres
    port : int -- The port, defaults to 5433
    password : str -- The password, must be specified

    Returns:
    conn -- The connection to the database
    '''
    return psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
