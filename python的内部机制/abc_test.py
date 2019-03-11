from collections.abc import Sized
from abc import ABCMeta, abstractmethod
# abc是Abstract Base Class类的缩写
# 主要应用场景有两个：①判断某个对象是否为某种类型 ②为某些特定的类指定必须实现某些特定的方法


class DefinedClass:
    def __init__(self):
        pass

    def __len__(self):
        return 3


defined_class = DefinedClass()
print(isinstance(defined_class, Sized))

# 为某些特定的类指定必须实现某些特定的方法
# 两种实现方法


class CacheBase:
    """
    第一种实现方法直接抛出 NotImplementedError
    这种实现方法的问题是：如果子类未实现，只有调用set()或get()方法才报错，对象可以正确的被实例化出来
    """
    def set(self):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError


class CacheBaseType(metaclass=ABCMeta):
    """
    使用ABCMeta，如果子类未实现抽象方法，则无法实例化对象，会报错
    """
    @abstractmethod
    def set(self):
        pass

    @abstractmethod
    def get(self):
        pass


class RedisCache(CacheBase):
    pass


class RedisCacheType(CacheBaseType):
    pass


redis_cache = RedisCache()
# 调用时才报错
redis_cache.set()
# 实例化时就报错
redis_cache_type = RedisCacheType()
