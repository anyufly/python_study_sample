from collections import OrderedDict

# python3 下的dict也是有序的， Python2中的是无序的
# 会保持元素定义的顺序 {'a':1, 'b':2, 'c':3}
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)

# 顺序变为 {'a':1, 'c':3, 'b':2}
ordered_dict.move_to_end('b')
print(ordered_dict)
