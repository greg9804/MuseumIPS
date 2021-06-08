

class Search:
    def __init__(self, params, coll):
        self.params = params
        self.coll = coll


    def start(self):
        result = set()
        for k, v in self.params.items():
            #передавать вниз по течению только то что уже найдено и отсеивать
            #оздать список и добавлять в него, каждый этап поиска должен отсеивать лишнее
            #поиск по названию
            if (k == "searchLine"):
                result.update(self.byName(v))
            #поиск по месту создания
            elif (k == "cb"):
                result.update(self.byPlace(v))
            #поиск по примечанию
            elif (k == "note"):
                result.update(self.byNote(v))

        # поиск по годам создания на вхождение в отрезок
        if "yearbegin" in self.params and "yearend" in self.params:
            result.update(self.betwenYears(self.params["yearbegin"], self.params["yearend"]))
        elif "yearbegin" in self.params and "yearend" not in self.params:
            result.update(self.moreThenYear(self.params["yearbegin"]))
        elif "yearbegin" not in self.params and "yearend" in self.params:
            result.update(self.lessThenYear(self.params["yearend"]))

        #поиск по дате поступления на вхождение в отрезок
        if "datein_begin" in self.params and "datein_end" in self.params:
            pass

        for x in result:
            print("Найден:", x)
        print("-------------------------------------")

    def byName(self, value):
        lst = []
        for avtor, exponats in self.coll.collection.items():
            for e in exponats:
                if (e.name.startswith(value)):
                    lst.append(e)
        return lst

    def byPlace(self, value):
        lst = []
        for avtor, exponats in self.coll.collection.items():
            for e in exponats:
                if (e.place.startswith(value)):
                    lst.append(e)
        return lst

    def byNote(self, value):
        lst = []
        for avtor, exponats in self.coll.collection.items():
            for e in exponats:
                if (e.note.find(value) != -1):
                    lst.append(e)
        return lst

    def betwenYears(self, year_begin, year_end):
        lst = []
        yb = int(year_begin)
        ye = int(year_end)
        for avtor, exponats in self.coll.collection.items():
            for e in exponats:
                e_y = int(e.year)
                if yb <= e_y <= ye:
                    lst.append(e)
        return lst

    def moreThenYear(self, year_begin):
        lst = []
        ye = int(year_begin.split(".")[2])
        for avtor, exponats in self.coll.collection.items():
            for e in exponats:
                e_y = int(e.year)
                if e_y >= ye:
                    lst.append(e)
        return lst

    def lessThenYear(self, year_end):
        lst = []
        yb = int(year_end.split(".")[2])
        for avtor, exponats in self.coll.collection.items():
            for e in exponats:
                e_y = int(e.year)
                if e_y <= yb:
                    lst.append(e)
        return lst
