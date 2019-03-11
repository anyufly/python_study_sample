from datetime import date, datetime


class User:
    def __init__(self, name: str, birthday: date):
        self.name = name
        self.birthday = birthday
        self._age = 0
        # self._age = self.get_age()

    def get_age(self):
        return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return self.get_age()

    @age.setter
    def age(self, value):
        self._age = value

    @age.deleter
    def age(self):
        del self._age


if __name__ == '__main__':
    # 25
    user_sample = User('jeff', date(1993, 9, 24))
    print(user_sample.age)

    user_sample.age = 30
    # 25
    print(user_sample.age)
    # 30
    print(user_sample._age)

    del user_sample.age
    # 25
    print(user_sample.age)
    # not found
    print(user_sample._age)
