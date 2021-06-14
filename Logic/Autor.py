class Autor:
    """Является представлением реального объекта автор экспоната

    o	полное имя
    o	дата рождения
    o	дата смерти
    o	количество прожитых лет (вычисляемое поле)
    o	страна проживания (выбирается из справочника)

    """
    def __init__(self, id, fullname, birthday, deathday, years, country):
        self.id = id
        self.fullname = fullname
        self.birthday = birthday
        self.deathday = deathday
        self.years = years
        self.country = country

    def __str__(self):
        return f"{self.id},{self.fullname},{self.birthday.toString('yyyy-MM-dd')},{self.deathday.toString('yyyy-MM-dd')},{self.years},{self.country}"

    def get_id(self):
        return self.id;

