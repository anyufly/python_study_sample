'''
内置变量 package、name、file、doc
当模块为入口文件是 __name__的值为 __main__
'''

# a = 1
# b = 2
# infos = dir()
# print(infos)
print('package: ' + (__package__ or '当前模块没有包'))
print('name:    ' + __name__)
print('doc: ' + __doc__ or '当前模块没有文档注释')
print('file:    ' + __file__)
print("=============分割线===============")
