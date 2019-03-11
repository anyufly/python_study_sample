from collections import Counter
# Counter用于数量统计
# Counter 继承于 dict
# 传入一个可迭代对象
user_counter = Counter([1, 2, 3, 1, 4, 6, 7])
print(user_counter)
user_counter = Counter('I have a Dreams!')
print(user_counter)
# 与之前的统计序列合并
user_counter.update([1, 3, 5, 'g'])
print(user_counter)
# 获取最常出现的前两位元素
# [(' ', 3), ('a', 3)]
print(user_counter.most_common(2))
