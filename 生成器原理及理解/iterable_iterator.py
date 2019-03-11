class CustomIterator:

    def __init__(self, data):
        self.data = data
        self.index = 0

    # 如果是迭代器，直接
    def __iter__(self):
        return self

    # 同时实现__iter__和__next__魔法函数则该对象就是一个迭代器， __next__魔法函数返回迭代器的下一个值
    # 当迭代器中所有值都获取完时，需要抛出StopIteration
    def __next__(self):
        try:
            result = self.data[self.index]
            self.index += 1
            return result
        except IndexError:
            raise StopIteration


class Company:

    def __init__(self, employee_list):
        self.employee_list = employee_list

    # 实现了魔法函数__iter__即为可迭代对象，该魔法函数需要返回一个迭代器， 使用iter()函数时会调用这个方法
    def __iter__(self):
        return CustomIterator(self.employee_list)


if __name__ == '__main__':
    company = Company(['Jeff', 'Rose', 'Mary'])

    company_iterator = iter(company)
    # for 循环原理，一直调用迭代器的next()函数，直到捕获StopIteration异常
    while True:
        try:
            print(next(company_iterator))
        except StopIteration:
            break

    for i in company:
        print(i)
