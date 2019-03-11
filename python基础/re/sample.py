import re

a = 'C0C++7J3H^^7&MKSDGJcdfgrtLLkdjfgh334KKLIU   \
        s45fgkldfylktyklrwre8rerfkxcve3'
b = 'pytho0python1pythonn2pytyonnn3'
result = re.findall('\s{2}\w{3,6}?', a)
print(result)

a = re.findall('python*?', b)
d = re.findall('python+?', b)
c = re.findall('python??', b)
print(a, d, c)
