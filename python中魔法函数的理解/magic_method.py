class BookCollections:
    """
    魔法函数示例
    """
    def __init__(self, book_list):
        """
        构造方法：定义一个变量 book_list
        """
        self.book_list = book_list

    def __getitem__(self, item):
        """
        实现魔法函数__getitem__，使对象可以进行迭代、切片（成为序列）
        :param item:
        :return:
        """
        return self.book_list[item]

    def __len__(self):
        """
        实现魔法函数__len__，使对象可以在外部调用len()函数获取长度
        :return:
        """

        return len(self.book_list)


book_collection = BookCollections(['追风筝的人', '不能承受的生命之轻', '皮囊'])
book_collection1 = book_collection[:2]

# 实现 __getitem__魔法函数后，对象成为序列类型 可迭代、切片
for i in book_collection:
    print(i)

for i in book_collection1:
    print(i)

# 实现魔法函数__len__，使对象可以在外部调用len()函数获取长度
print(len(book_collection))
