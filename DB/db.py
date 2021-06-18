import sqlite3
import sys
import traceback

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox


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

    def insertExpo(self, expo_s):
        try:
            connection = sqlite3.connect("DB/museum.db")
            cur = connection.cursor()

            expo = expo_s.split(",")
            id = expo[0]
            name = expo[1]
            autor = expo[2]
            type = expo[3]
            style = expo[4]
            year = expo[5]
            place = expo[6]
            date_in = expo[7]
            adm = expo[8]
            demo = expo[9]
            note = expo[10]

            query = "INSERT INTO exponats VALUES ({}, '{}', {}, {}, {}, {}, '{}', date('{}'), {}, {}, '{}')".format(id, name, autor, type, style, year, place, date_in, adm, demo, note)
            print(query, file=sys.stderr)
            cur.execute(query)

            connection.commit()
            connection.close()
            return True

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Не верный файл! Запрос не выполнен!")
            msg.setInformativeText('SQLite error: %s' % (' '.join(er.args)))
            msg.setWindowTitle("Error")
            msg.exec_()
            return False

