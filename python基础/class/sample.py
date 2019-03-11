class Student(object):
    name = ''
    age = 0

    # def __init__(self):
    #     print(name)
    # 构造方法不能重载
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def do_homework(self):
        print(self.name)
        print('do homework')

# student1 = Student()

