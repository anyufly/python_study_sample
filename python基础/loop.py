# 循环
# while for

i = 0
while i <= 5:
    print(i, end=' ')
    i += 1
else:
    print("\nFinish")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in a:
    print(i, end=' ')
print('\n')

print(a[0::2])
print('\n')

for i in range(0, len(a), 2):
    print(a[i], end=' ')
print('\n')

b = [[1, 2, 3, 4, 5, 6, 7], [2, 4, 6, 8, 10], (1, 2, 3, 4)]

for x in b:
    if isinstance(x, tuple):
        print('tuple break!!!')
        break
    for y in x:
        if y == 3:
            continue
        print(y, end=' ')
    else:
        print("\ninner")
else:
    print("\nouter")
