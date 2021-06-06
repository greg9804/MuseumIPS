from DB.db import DB


class Collection:
    """ Коллекция автор : {экспонаты} """
    def __init__(self):
        self.collection = dict()
        self.db = DB()

    def load(self):
        self.loadAutors()
        self.loadExponats()

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
        pass

    def printCollection(self):
        for key, value in self.collection:
            print(key, value)
