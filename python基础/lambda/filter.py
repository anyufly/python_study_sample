a = [1, 2, 3, 4, 5, 6, 7]

result = filter(lambda x: True if x % 2 == 1 else False, a)
print(list(result))
