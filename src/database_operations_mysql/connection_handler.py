import mysql.connector

class ConnectionHandler:
    def __init__(self, host='localhost', user='root', password='password', db='Employee', table='users'):
        # Initialize class attributes with the provided values
        self._host = host
        self._user = user
        self._password = password
        self._db = db
        self._table = table
        self.conn = None
        self.cursor = None

    # Properties for controlled access to private attributes
    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        if isinstance(value, str):
            self._host = value
        else:
            raise ValueError("Host must be a string.")

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, value):
        if isinstance(value, str):
            self._db = value
        else:
            raise ValueError("Database name must be a string.")

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, value):
        if isinstance(value, str):
            self._table = value
        else:
            raise ValueError("Table name must be a string.")

    def get_connection(self):
        """Establish and return a connection to the MySQL database."""
        try:
            # Establish connection
            self.conn = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password
            )
            self.cursor = self.conn.cursor()

            # Create database if it doesn't exist
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self._db}")

            # Use the created or existing database
            self.cursor.execute(f"USE {self._db}")

            # Create table if it doesn't exist
            self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self._table} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                age INT
            )
            """)

            # Commit changes and return connection and cursor
            self.conn.commit()
            print(f"Connection established to database '{self._db}' and table '{self._table}'.")
            return self.conn, self.cursor
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None, None

    def close_connection(self):
        """Close the cursor and the connection safely."""
        if self.cursor:
            self.cursor.close()
            print("Cursor closed.")
        if self.conn:
            self.conn.close()
            print("Connection closed.")

    def get_db_info(self):
        """Return a dictionary containing database and table info."""
        return {'host': self._host, 'db': self._db, 'table': self._table}


