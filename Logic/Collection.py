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
        self.print()

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
        for t in tuples:
            id = t[0]
            fullname = t[1]
            birthday = t[2]
            deathday = t[3]
            years = t[4]
            country = self.takeValueFromRefById(t[5], self.countriesList)
            self.Autors.append(Autor(id, fullname, birthday, deathday, years, country))

    def parseExponats(self, tuples):
        for t in tuples:
            id = t[0]
            name = t[1]
            avtor = self.findAutorById(t[2])
            type = self.takeValueFromRefById(t[3], self.typesList)
            style = self.takeValueFromRefById(t[4], self.stylesList)
            year = t[5]
            place = t[6]
            datein = t[7]
            admission = self.takeValueFromRefById(t[8], self.admissionsList)
            demo = self.takeValueFromRefById(t[9], self.demosList)
            note = t[10]
            self.Exponats.append(Exponat(id, name, avtor, type, style, year, place, datein, admission, demo, note))

    def addAutor(self, autor):
        if autor not in self.collection:
            self.collection[autor] = []

    def addExpo(self, autor, expo):
        itms = list(self.collection[autor])
        itms.append(expo)
        self.collection[autor] = itms

    def loadAutors(self):
        print(self.db.getAutors())

    def loadExponats(self):
        print(self.db.getExponats())

    def printCollection(self):
        for key, value in self.collection:
            print(key, value)
