# -*- coding: utf-8 -*-
# from collections import UserDict


# 不推荐直接继承dict，可能会有未知BUG
# 如果要继承Dict，推荐使用UserDict
class CustomDict(dict):

    def __getitem__(self, item):
        return super(CustomDict, self).__getitem__(item)

    def __setitem__(self, key, value):
        super(CustomDict, self).__setitem__(key, value * 2)

    def __missing__(self, key):
        try:
            return self.__getitem__(key)
        except RuntimeError:
            self.__setitem__(key, 0)
            return self.__getitem__(key)


custom_dict = CustomDict()
custom_dict['d'] = 2

print(custom_dict)
print(custom_dict['d'])
print(custom_dict['e'])
