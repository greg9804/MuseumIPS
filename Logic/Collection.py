from PySide6.QtCore import QDate

from DB.db import DB
from Logic.Autor import Autor
from Logic.Exponat import Exponat


class Collection:
    """ Коллекция автор : {экспонаты} и справочники"""
    def __init__(self):
        self.collection = dict()
        self.db = DB()
        self.Autors = []
        self.Exponats = []

    def load(self):
        self.admissionsList = self.db.getTableWithName('admissions')
        self.countriesList = self.db.getTableWithName('countries')
        self.demosList = self.db.getTableWithName('demos')
        self.stylesList = self.db.getTableWithName('styles')
        self.typesList = self.db.getTableWithName('types')
        self.autorsList = self.db.getTableWithName('autors')
        self.exponatsList = self.db.getTableWithName('exponats')
        self.parse()
        self.createCollection()
        self.printCollection()

    def parse(self):
        self.parseAutors(self.autorsList)
        self.parseExponats(self.exponatsList)

    def print(self):
        print("Autors:")
        for a in self.Autors:
            print(a)
        print("---------")
        print("Exponats:")
        for e in self.Exponats:
            print(e)

    def takeValueFromRefById(self, id, ref):
        """ Достает из справочника значение по id """
        for r in ref:
            if r[0] == id:
                return r[1]

    def findAutorById(self, id):
        for a in self.Autors:
            if a.id == id:
                return a

    def parseAutors(self, tuples):
        self.Autors.clear()
        for t in tuples:
            id = t[0]
            fullname = t[1]

            y, m, d = int(t[2].split("-")[0]), int(t[2].split("-")[1]), int(t[2].split("-")[2])
            birthdate = QDate()
            birthdate.setDate(y, m, d)
            birthday = birthdate


            y, m, d = int(t[3].split("-")[0]), int(t[3].split("-")[1]), int(t[3].split("-")[2])
            deathdate = QDate()
            deathdate.setDate(y, m, d)
            deathday = birthdate

            years = t[4]
            country = self.takeValueFromRefById(t[5], self.countriesList)
            self.Autors.append(Autor(id, fullname, birthday, deathday, years, country))

    def parseExponats(self, tuples):
        self.Exponats.clear()
        for t in tuples:
            id = t[0]
            name = t[1]
            avtor = self.findAutorById(t[2])
            type = self.takeValueFromRefById(t[3], self.typesList)
            style = self.takeValueFromRefById(t[4], self.stylesList)
            year = t[5]
            place = t[6]

            y, m, d = int(t[7].split("-")[0]), int(t[7].split("-")[1]), int(t[7].split("-")[2])
            dt = QDate()
            dt.setDate(y, m, d)
            datein = dt

            admission = self.takeValueFromRefById(t[8], self.admissionsList)
            demo = self.takeValueFromRefById(t[9], self.demosList)
            note = t[10]
            self.Exponats.append(Exponat(id, name, avtor, type, style, year, place, datein, admission, demo, note))

    def createCollection(self):
        self.collection.clear()
        for e in self.Exponats:
            autor = e.autor
            if autor in self.collection:
                s = set(self.collection.get(autor))
                s.add(e)
                self.collection[autor] = s
            elif autor not in self.collection:
                s = set()
                s.add(e)
                self.collection[autor] = s

    def printCollection(self):
        for pair in self.collection.items():
            print('Для %s' % (pair[0]))
            for s in pair[1]:
                print(s)

    def getCountriesForCB(self):
        lst = []
        for c in self.countriesList:
            lst.append(c[1])
        return lst