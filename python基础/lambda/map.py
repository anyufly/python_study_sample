a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [2, 4, 6, 8, 10, 12, 14]

result = map(lambda x, y: x + y, a, b)
print(list(result))

a = {'name': 'jeff', 'age': 18, 'married': False}
b = {'name': 'jeff', 'age': 18}

custom_map = map(lambda x, y: x if x == y else None, a.keys(), b.keys())
print(list(custom_map))
