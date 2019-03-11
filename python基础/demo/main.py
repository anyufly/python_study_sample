# 入口文件中只能使用绝对引入，不能使用相对引入 因为入口文件中的__name__变量被Python修改为__main__
# from demo.package2.package4 import module1
# 将入口文件视为模块运行需要进入上一层目录 使用 pytyon -m 命名空间 命令运行
from package2.package4 import module1
print('--------------------main--------------------')
print('main:    ' + (__package__ or '入口文件，没有包'))
