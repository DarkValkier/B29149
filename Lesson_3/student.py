import datetime


class Student:
    name = ''
    birth_year = 0
    group = ''
    mark = .0

    # Конструктор (метода __init__)

    # Метод __str__

    def get_age(self):
        return datetime.date.today().year - self.birth_year
