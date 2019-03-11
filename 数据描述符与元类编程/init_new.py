class Student:

    def __new__(cls, *args, **kwargs):
        # args = ('Jeff', )
        kwargs['age'] = 18
        kwargs['birthday'] = '1991-05-21'
        obj = super().__new__(cls)
        print("====__new__====")
        print(id(obj))
        # print(id(args))
        print(id(kwargs))
        return obj

    def __init__(self, *args, **kwargs):
        print("====__init__====")
        print(id(self))
        # print(id(args))
        print(id(kwargs))
        param = ['name', 'age', 'birthday']

        for i in range(0, len(args)):
            setattr(self, param[i], args[i])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        name = self.name
        age = self.age
        birthday = self.birthday or ''
        return f'name：{name}\tage：{age}\tbirthday:{birthday}'


if __name__ == '__main__':
    student = Student('Rose', birthday='1993-09-24', age=19)
    print(student)
