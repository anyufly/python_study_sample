# from Student import *
from Student import Student

s = Student('jeff', 18)
s.get_name()
print(s._name)
print(s.__dict__)
print(dir(s))

# 单下划线开头的变量不能 "from mudule import *" 被导入，
# 单下划线开头的类成员变量与public的成员变量的可见性相同
# NameError: name '_never_import' is not defined
# print(_never_import)
