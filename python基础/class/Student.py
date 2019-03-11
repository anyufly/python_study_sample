'''
Student类
'''
from Human import Human

_never_import = '单下划线开头不能 "from mudule import *" 被导入？'


class Student(Human):
    def __init__(self, name, age):
        super(Student, self).__init__(name, age)

    def get_name(self):
        print(self._name)
