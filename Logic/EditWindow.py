from PySide6 import QtWidgets, QtSql, QtCore
from PySide6.QtWidgets import QVBoxLayout, QComboBox


class EditWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        #ДОБАВИТЬ КОД ПО УЛУЧШЕНИЮ СТИЛЯ И ДЕЙСТВИЕ ПРИ ЗАКРЫТИИ

        # Connect to database
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('DB/museum.db')
        self.db.open()

        self.layout = QVBoxLayout(self)

        self.table_names = QComboBox(self)
        self.table_names.addItems(self.db.tables())

        self.table_view = QtWidgets.QTableView(self)
        self.table_model = QtSql.QSqlTableModel(self, self.db)
        self.table_view.setModel(self.table_model)

        self.delegate = SqlItemDelegate(self.db, self)
        self.table_view.setItemDelegate(self.delegate)

        self.table_names.currentTextChanged.connect(self.table_model.setTable)
        self.table_names.currentTextChanged.connect(self.table_model.select)

        self.table_names.currentTextChanged.connect(self.delegate.setTable)
        self.insert = QtWidgets.QPushButton('Insert', self)
        self.insert.clicked.connect(self.insertRow)
        self.delete = QtWidgets.QPushButton('Delete', self)
        self.delete.clicked.connect(self.deleteRow)

        self.layout.addWidget(self.table_view)
        self.layout.addWidget(self.table_names)
        self.layout.addWidget(self.insert)
        self.layout.addWidget(self.delete)

    def deleteRow(self):
        index = self.table_view.currentIndex()
        self.table_model.removeRows(index.row(), 1)

    def insertRow(self):
        self.table_model.insertRows(0, 1)


class SqlItemDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, database, parent=None):
        QtWidgets.QStyledItemDelegate.__init__(self, parent)
        self.__table__ = ''
        self.__database__ = database

    def setTable(self, table):
        self.__table__ = table

    def createEditor(self, parent, option, index):
        record = self.__database__.record(self.__table__)
        '''
        column_type = record.field(record.fieldName(index.column())).type()

        print(record.fieldName(index.column()), column_type)
        if column_type == QtCore.QVariant.Double:
            return QtWidgets.QDoubleSpinBox(parent)
        if column_type == QtCore.QVariant.DateTime:
            return QtWidgets.QDateTimeEditor(parent)
        # etc.
        '''

        return QtWidgets.QStyledItemDelegate.createEditor(self, parent, option, index)

