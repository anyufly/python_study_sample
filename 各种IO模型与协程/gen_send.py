

def gen():
    a = yield 1
    print(a)
    try:
        yield 2
    except Exception:
        pass
    yield 3


if __name__ == '__main__':
    g = gen()
    print(g.send(None))
    print(g.send(11))
    print(g.throw(Exception, '111'))
    # print(next(g))
