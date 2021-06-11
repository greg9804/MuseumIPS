from PySide6.QtWidgets import QButtonGroup

class Statistics:
    """
        Дать пользователю представление о количестве экспонатов по различным критериям
        количества экспонатов для каждого автора,
        типа, стиля, года создания,
        способа поступления в музей,
        места демонстрации/хранения

        либо по одному вывести в программе (listWidget, либо экспортировать всю в файл)
    """
    def __init__(self, coll):
        self.coll = coll

    def build(self, id_button):
        result = []
        if id_button == -2:
            result.extend(self.buildByAutor())
        elif id_button == -3:
            result.extend(self.buildByType())
        elif id_button == -4:
            result.extend(self.buildByStyle())
        elif id_button == -5:
            result.extend(self.buildByYear())
        elif id_button == -6:
            result.extend(self.buildByAdmission())
        elif id_button == -7:
            result.extend(self.buildByDemo())

        return result

    def buildToFile(self):
        result = []
        result.extend(self.buildByAutor())
        result.extend(self.buildByType())
        result.extend(self.buildByStyle())
        result.extend(self.buildByYear())
        result.extend(self.buildByAdmission())
        result.extend(self.buildByDemo())

        return result


    def buildByAutor(self):
        lst = []
        for autor, exponats in self.coll.collection.items():
            pair = (autor.fullname, len(exponats))
            lst.append(pair)

        return lst

    def buildByType(self):
        lst = []
        for t in self.coll.typesList:
            count_t = 0
            for e in self.coll.Exponats:
                if t[1] == e.type:
                    count_t += 1
            lst.append((t[1], count_t))

        return lst

    def buildByStyle(self):
        lst = []
        for s in self.coll.stylesList:
            count_s = 0
            for e in self.coll.Exponats:
                if s[1] == e.style:
                    count_s += 1
            lst.append((s[1], count_s))

        return lst

    def buildByYear(self):
        lst = {}
        for e in self.coll.Exponats:
            if e.year in lst:
                lst[e.year] += 1
            if e.year not in lst:
                lst[e.year] = 1
        res = []
        for i in lst.items():
            res.append((i[0], i[1]))

        return res

    def buildByAdmission(self):
        lst = []
        for adm in self.coll.admissionsList:
            count_adm = 0
            for e in self.coll.Exponats:
                if adm[1] == e.admission:
                    count_adm += 1
            lst.append((adm[1], count_adm))

        return lst

    def buildByDemo(self):
        lst = []
        for dm in self.coll.demosList:
            count_dm = 0
            for e in self.coll.Exponats:
                if dm[1] == e.demo:
                    count_dm += 1
            lst.append((dm[1], count_dm))

        return lst


