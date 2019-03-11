from collections.abc import MutableSequence


# 序列在abc模块中的抽象基类是：Sequence(Reversible, Collection)
# Sequence 是Reversible和Collection的子类 Collection是 Sized、Iterable、Container
# 的子类,实现一个自定义的Sequence需要实现他们个自定义的抽象方法
# __getitem__（Sequence）、__reversed__（Reversible）、__len__（Sized）
# __iter__（Iterable）、__contains__（Container）
# 可变序列是MutableSequence(Sequence)，实现一个自定义的MutableSequence还需实现
# __setitem__()、__delitem__()、insert()
class CustomMutableSequence:

    def __init__(self, custom_sequence: MutableSequence):
        self.custom_sequence = custom_sequence

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.__class__((self.custom_sequence[item]))
        elif isinstance(item, int):
            return self.custom_sequence[item]

    def __reversed__(self):
        return self.__class__(type(self.custom_sequence)((reversed(self.custom_sequence))))

    def __len__(self):
        return len(self.custom_sequence)

    def __iter__(self):
        return iter(self.custom_sequence)

    def __contains__(self, x):
        return x in self.custom_sequence

    def __setitem__(self, index, value):
        self.custom_sequence[index] = value

    def __delitem__(self, index):
        del self.custom_sequence[index]

    def insert(self, index, value):
        self.custom_sequence.insert(index, value)

    def __str__(self):
        return 'CustomMutableSequence(' + str(self.custom_sequence) + ')'


my_sequence = CustomMutableSequence(['jeff', 'lisa', 'mary', 'jack', 'rose'])

print(my_sequence[2])
print(my_sequence[0::2])
my_sequence[4] = 'alexa'
print(my_sequence)
my_sequence.insert(5, 'stark')
print(my_sequence)
print(reversed(my_sequence))

del my_sequence[5]
print(my_sequence)

for i in my_sequence:
    print(i)

