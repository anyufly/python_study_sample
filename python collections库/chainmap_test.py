from collections import ChainMap

# 可以将dict进行合并操作
dict1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

dict2 = {
    'b': 3,
    'd': 4,
    'f': 5
}

chain_map = ChainMap(dict1, dict2)
# 若操作的多个字典中含有相同key的元素，则会取第一次出现的元素
for key, value in chain_map.items():
    print(key + '：' + str(value))

print('=======================================================')

# 可以使用new_child方法添加新的dict(生成一个新的对象)
new_chain_map = chain_map.new_child({
    'g': 6,
    'h': 7
})

for key, value in new_chain_map.items():
    print(key + '：' + str(value))


print(new_chain_map.maps)
# map中的元素指向的是原字典，不会生成一个新对象
# True
print(id(new_chain_map.maps[1]) == id(dict1))

new_chain_map.maps[1]['a'] = 2
print(new_chain_map)
# {'a': 2, 'b': 2, 'c': 3}
print(dict1)
