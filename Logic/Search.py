from PySide6.QtCore import QDate


class Search:
    def __init__(self, params, exponats):
        self.params = params
        self.exponats = exponats


    def start(self):
        result = self.exponats.copy()
        for k, v in self.params.items():
            #передавать вниз по течению только то что уже найдено и отсеивать
            #каждый этап поиска должен отсеивать лишнее
            #поиск по названию
            if (k == "searchLine"):
                result = self.byName(v, result)
            #поиск по месту создания
            elif (k == "cb"):
                result = self.byPlace(v, result)
            #поиск по примечанию
            elif (k == "note"):
                result = self.byNote(v, result)

        # поиск по годам создания на вхождение в отрезок
        if "yearbegin" in self.params and "yearend" in self.params:
            result = self.betwenYears(self.params["yearbegin"], self.params["yearend"], result)
        elif "yearbegin" in self.params and "yearend" not in self.params:
            result = self.moreThenYear(self.params["yearbegin"], result)
        elif "yearbegin" not in self.params and "yearend" in self.params:
            result = self.lessThenYear(self.params["yearend"], result)

        #поиск по дате поступления на вхождение в отрезок
        if "datein_begin" in self.params and "datein_end" in self.params:
            result = self.betwenDates(self.params["datein_begin"], self.params["datein_end"], result)
        elif "datein_begin" in self.params and "datein_end" not in self.params:
            result = self.moreThenDate(self.params["datein_begin"], result)
        elif "datein_begin" not in self.params and "datein_end" in self.params:
            result = self.lessThenDate(self.params["datein_end"], result)

        finded = []
        for x in result:
            print("Найден:", x)
            finded.append(x)
        print("-------------------------------------")
        return finded

    def byName(self, value, exponats):
        exponats = filter(lambda e: e.name.startswith(value), exponats)
        return exponats

    def byPlace(self, value, exponats):
        exponats = filter(lambda e: e.place == value, exponats)
        return exponats

    def byNote(self, value, exponats):
        exponats = filter(lambda e: e.note.startswith(value), exponats)
        return exponats

    def betwenYears(self, year_begin, year_end, exponats):
        yb = int(year_begin)
        ye = int(year_end)
        exponats = filter(lambda e: yb <= int(e.year) <= ye, exponats)
        return exponats

    def moreThenYear(self, year_begin, exponats):
        yb = int(year_begin)
        exponats = filter(lambda e: int(e.year) >= yb, exponats)
        return exponats

    def lessThenYear(self, year_end, exponats):
        ye = int(year_end)
        exponats = filter(lambda e: int(e.year) <= ye, exponats)
        return exponats

    def betwenDates(self, date, date2, exponats):
        d, m, y = int(date.split(".")[0]), int(date.split(".")[1]), int(date.split(".")[2])
        date = QDate()
        date.setDate(y, m, d)
        d2, m2, y2 = int(date2.split(".")[0]), int(date2.split(".")[1]), int(date2.split(".")[2])
        date2 = QDate()
        date2.setDate(y2, m2, d2)
        exponats = filter(lambda e: date <= e.date_in <= date2, exponats)
        return exponats

    def moreThenDate(self, date, exponats):
        d, m, y = int(date.split(".")[0]), int(date.split(".")[1]), int(date.split(".")[2])
        date = QDate()
        date.setDate(y, m, d)
        print(date)
        exponats = filter(lambda e: e.date_in >= date, exponats)
        return exponats


    def lessThenDate(self, date, exponats):
        d, m, y = int(date.split(".")[0]), int(date.split(".")[1]), int(date.split(".")[2])
        date = QDate()
        date.setDate(y, m, d)
        print(date)
        exponats = filter(lambda e: e.date_in <= date, exponats)
        return exponats
