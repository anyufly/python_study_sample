import re
a = 'javaC#JavaScript.NetC#PealLisp23h4565jl65jljjhdf44k5kll54'
b = a.replace('C#', 'GO')
c = re.sub('c#', 'GO', a, count=1, flags=re.I)


def convert(value):
    matches = value.group()
    if int(matches) <= 50:
        return 'L'
    else:
        return 'G'


d = re.sub('\d{2}', convert, a)
print(b)
print(c)
print(d)
