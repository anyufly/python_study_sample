position = 0


def tourist(first_position):
    def go(*offsets):
        nonlocal first_position
        offset_count = len(offsets)
        for i in range(0, offset_count):
            offset = offsets[i]
            yield first_position
            first_position += offset
            if i == offset_count - 1:
                yield first_position
    return move


def move(*offsets):
    global position
    offset_count = len(offsets)
    for i in range(0, offset_count):
        yield position
        offset = offsets[i]
        position += offset
        if i == offset_count - 1:
            yield position


pos_gen = move(1, -2, 3, 4, -6)
for pos in pos_gen:
    print(pos)
print('position：' + str(position))

closure_gen_func = tourist(position)
closure_gen = closure_gen_func(1, -2, 3, 4, -7)
for pos in closure_gen:
    print(pos)

print('position：' + str(position))