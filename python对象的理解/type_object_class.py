a = 1
b = "abc"


class Student:
    pass


stu = Student()

# <class 'int'>
print(type(1))
# <class 'type'>
print(type(int))

# <class 'str'>
print(type(b))
# <class 'type'>
print(type(str))

# <class '__main__.Student'>
print(type(stu))
# <class 'type'>
print(type(Student))

# <class 'type'>
print(type(object))
# <class 'type'>
print(type(type))

# (<class 'object'>,)
print(int.__bases__)
# (<class 'object'>,)
print(str.__bases__)
# (<class 'object'>,)
print(Student.__bases__)
# (<class 'object'>,)
print(type.__bases__)
# ()
print(object.__bases__)