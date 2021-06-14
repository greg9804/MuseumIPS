

class Exponat:
    """
    Является представлением реального объекта экспонат

    o	название
    o	автор (выбирается из таблицы авторов)
    o	тип (выбирается из списка, например: картина, скульптура, предмет мебели и т.д.)
    o	стиль (выбирается из справочника; например: ампир, барокко, модернизм и т.д.)
    o	год создания,
    o	место создания
    o	дата поступления в музей
    o	как попал в музей (выбирается из списка; например: куплен, подарен, передан на хранение)
    o	место демонстрации или хранения (выбирается из справочника)
    o	примечание

    """
    def __init__(self, id, name, autor, type, style, year, place, date_in, admission, demo, note):
        self.id = id
        self.name = name
        self.autor = autor
        self.type = type
        self.style = style
        self.year = year
        self.place = place
        self.date_in = date_in
        self.admission = admission
        self.demo = demo
        self.note = note

    def __str__(self):
        return f"{self.id} {self.name} //{self.autor.fullname}// {self.type} {self.style} {self.year} {self.place} {self.date_in} {self.admission} {self.demo} {self.note}"

    def getStringToSaveForFile(self, coll):
        type_id = self.getTypeId(coll)
        style_id = self.getStyleId(coll)
        adm_id = self.getAdmId(coll)
        demo_id = self.getDemoId(coll)

        return f"{self.id},{self.name},//{self.autor.get_id()}//,{type_id},{style_id},{self.year},{self.place},{self.date_in.toString('yyyy-MM-dd')},{adm_id},{demo_id},{self.note}"

    def getTypeId(self, coll):
        for e in coll.typesList:
            if self.type == e[1]:
                return e[0]

    def getStyleId(self, coll):
        for e in coll.stylesList:
            if self.style == e[1]:
                return e[0]

    def getAdmId(self, coll):
        for e in coll.admissionsList:
            if self.admission == e[1]:
                return e[0]

    def getDemoId(self, coll):
        for e in coll.demosList:
            if self.demo == e[1]:
                return e[0]
