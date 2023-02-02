import sqlite3

class data:
    def __init__(self, database_name):
        self.connection = sqlite3.connect("./" + database_name)
        self.cursor = connection.cursor()