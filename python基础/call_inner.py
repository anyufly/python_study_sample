'''
入口文件
'''
import package3.inner_variable
print('package: ' + (__package__ or '当前模块没有包'))
print('name:    ' + __name__)
print('doc: ' + __doc__ or '当前模块没有文档注释')
print('file:    ' + __file__)
print("=============分割线===============")
