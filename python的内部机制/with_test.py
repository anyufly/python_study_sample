# 上下文管理协议需要使用两个魔法函数
# 可以看做是 try...finally的优化实现
# __enter__和__exit__
from contextlib import contextmanager


class Sample:

    def __enter__(self):
        # with 语句调用
        print('enter!')
        return self

    @staticmethod
    def processing():
        print('processing...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit!')


@contextmanager
# 需要装饰生成器对象
# from contextlib import contextmanager
def processing_context():
    print('enter!')
    yield
    print('exit!')


def processing():
    print('processing...')


if __name__ == '__main__':
    print("第一种实现方式，通过实现魔法函数__enter__()、__exit__():")
    # 将Sample类中的__enter__函数的返回值赋给sample
    with Sample() as sample:
        # print(sample)
        sample.processing()
    #     执行完成后自动调用Sample类中的__exit__()函数

    print("第二种实现方式，使用contextmanager装饰器:")
    with processing_context():
        processing()
