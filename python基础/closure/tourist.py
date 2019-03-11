def factory(a):
    def move(step):
        nonlocal a
        a += step
        return a
    return move


tourist = factory(0)
# print(b.__closure__)
print(tourist(3))
print(tourist(4))
print(tourist(5))

c = 0


def go(step):
    global c
    c += step
    return c


print(go(3))
print(go(4))
print(go(5))
