from collections import namedtuple

# namedtuple可以用于快速生成类对象
Sample = namedtuple('Sample', 'a,b,c')
sample = Sample(1, 2, 3)

User = namedtuple('User', ('name', 'age', 'gender', 'height'))
user_tuple = ('jeff', 18, 'male')
user_dict = {
    'name': 'jeff',
    'age': 18,
    'gender': 'male'
}

# user = User('jeff', 18, 'male', 178)
# user = User(*user_tuple, 178)
# user = User(**user_dict, height=178)
user = User._make(['jeff', 18, 'male', 178])
print(user.name, user.age)
print(user._asdict())
# namedtuple同时具有tuple的特性（切片、拆包等）
print(user[0:2], user[1])
print(*user)
pass
