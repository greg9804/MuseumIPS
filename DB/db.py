import sqlite3
import sys
import traceback


class DB:
    def getAutors(self):
        try:
            self.connection = sqlite3.connect("DB/museum.db")
            query = "SELECT * FROM autors"
            result = self.connection.execute(query)

            for row_number, row_data in enumerate(result):
                print(row_number)
                print(row_data)

            self.connection.close()

            return result
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))

    def getExponats(self):
        try:
            self.connection = sqlite3.connect("DB/museum.db")
            query = "SELECT * FROM exponats"
            result = self.connection.execute(query)

            for row_number, row_data in enumerate(result):
                print(row_number)
                print(row_data)

            self.connection.close()

            return result
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))

