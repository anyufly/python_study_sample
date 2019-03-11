from . import module5
from .. import module4
# 使用 . 表示当前路径、 ..表示上层路径、 ...表示上上层路径（以此类推）， 不能引入超过顶级包的模块
# 会报错不能引入超过顶级包的模块
# from ... import module3
from ..package5 import module6
modulename = 'module1'
print('--------------------' + modulename + '--------------------')
print(modulename + '    ' + (__package__ or '入口文件，没有包'))
