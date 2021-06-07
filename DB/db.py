import sqlite3
import sys
import traceback


class DB:
    def getTableWithName(self, tablename):
        """Возвращает список из tuple, который представляет собой строку из таблицы"""
        result = []
        try:
            connection = sqlite3.connect("DB/museum.db")
            query = 'SELECT * FROM %s' % (tablename)
            cursor = connection.execute(query)

            for row_number, row_data in enumerate(cursor):
                result.append(row_data)

            connection.close()

            return result
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))