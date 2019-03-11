a = [i for i in range(1, 11) if i >= 5]
print(a)

b = [(x, y) for x in range(
    1, 11) if x % 2 == 1 for y in range(1, 11) if y % 2 == 0]
print(b)

d = {'name': 'jeff', 'age': 18}
c = {key: value for key, value in d.items()}
print(c)

a = (1, 2, 3, 4, 5)
b = (i * 2 for i in a)
print(b)
