from collections import deque
import bisect

#  bisect 是python中用来管理已排序对象（list、deque）的一个模块
# 对于对象中已有的顺序，bisect不会更改，bisect只会维护使用 bisect.insort()或 bisect.insort_left()函数插入的元素的顺序
# bisect.insort()和bisect.insort_left()的区别是，当插入得到元素与对象中元素值相等时，
# bisect.insort()往对象中最后一个个目标元素的右边插入，而 bisect.insort_left()往对象中第一个目标元素的左边插入

# bisect.bisect()、bisect.bisect_left()获取元素在对象中应该被插入的位置，他们的区别是，当元素的值与对象中元素值相等时，
# bisect.bisect() 会返回对象中最后一个目标元素后面的位置，而bisect.bisect_left()会返回对象中第一个目标元素的位置

sort_object = deque((1, 2, 5, 4, 7, 6, 9))
bisect.insort(sort_object, 12)
bisect.insort(sort_object, 11)
# deque([1, 2, 5, 4, 7, 6, 9, 11, 11.0, 12])
bisect.insort(sort_object, 11.0)
# deque([1, 2, 5, 4, 7, 6, 9, 11.0, 11, 11.0, 12])
bisect.insort_left(sort_object, 11.00)
# deque([1, 2, 5, 4, 7, 6, 9, 11.0, 11, 11.0, 12])
print(sort_object)
#  10
print(bisect.bisect(sort_object, 11))
# 7
print(bisect.bisect_left(sort_object, 11))
