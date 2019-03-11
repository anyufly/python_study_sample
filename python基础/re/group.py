import re

a = ' life is short, i use python, i love python'
# match方法从字符串的第一位开始匹配，第一位不匹配，立即返回
b = re.match('life(.*)python(.*)python', a)
print(b)
# 此条语句输出为None
# print(b.group(1))
# print(b.group(2))

# search方法会搜索整个字符串，
c = re.search('life(.*)python(.*)python', a)
print(c.group(1))
print(c.group(2))
print(c.groups())

d = re.findall('life(.*)python(.*)python', a)
print(d)


e = '1shjdhas43hjkdfh43tksdjkf98238942390sdjkfsdkf490874573'
f = re.findall('\d+', e)
print(f)
