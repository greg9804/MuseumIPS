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
    def __init__(self, id, name, autor, type, style, year, place, data_in, admission, demo, note):
        self.id = id
        self.name = name
        self.autor = autor
        self.type = type
        self.style = style
        self.year = year
        self.place = place
        self.data_in = data_in
        self.admission = admission
        self.demo = demo
        self.note = note

    def __str__(self):
        return f"{self.id} {self.name} {self.autor} {self.type} {self.style} {self.year} {self.place} {self.data_in} {self.admission} {self.demo} {self.note}"