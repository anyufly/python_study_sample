class IntField:

    def __init__(self, positive=None):
        self.positive = positive
        self._values = {}

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("属性值必须设置为int类型")
        if self.positive:
            if value < 0:
                raise ValueError("属性值必须为正数")
        self._values[id(instance)] = value
        # self._value = value

    def __get__(self, instance, owner):
        # print("get value...")
        return self._values[id(instance)]

    def __delete__(self, instance):
        # print("delete value...")
        del self._values[id(instance)]


class CharField:
    def __init__(self):
        self._values = {}

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("属性值必须为str类型")
        self._values[id(instance)] = value
        print(self._values)

    def __get__(self, instance, owner):
        return self._values[id(instance)]

    def __delete__(self, instance):
        del self._values[id(instance)]


class Student:

    name = CharField()
    age = IntField(positive=True)
    height = IntField(positive=True)

    def __init__(self, data: dict):
        self.data = data

    def __getattr__(self, item):
        try:
            return self.data[item]
        except KeyError:
            raise KeyError("找不到属性：" + str(item))

    # def __getattribute__(self, item):
    #     pass

    def __str__(self):
        return 'name：{name}\tage：{age}\theight：{height}\tschool：{school}'.format(
            name=self.name, age=self.age, height=self.height, school=self.school)


if __name__ == '__main__':
    student = Student({'school': '清华大学'})
    student.name = 'Jeff'
    student.age = 25
    student.height = 175

    student1 = Student({'school': '北京大学'})
    student1.name = 'Rose'
    student1.age = 26
    student1.height = 180

    print(student)
    print(student1)
