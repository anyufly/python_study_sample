class MyError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "异常：" + self.name

    def __repr__(self):
        return "异常：" + self.name


def catch_exception():
    try:
        raise MyError('心情不好，啥也不让你做！')
        print("I have a bad mood")
    except MyError as e:
        print(e)


catch_exception()
