import module1
# import subpackage.module3
import subpackage.module3 as module3
from module4 import module_name as module4_name
from subpackage import module5
from subpackage.module5 import module_name as module5_name
# 只会引入 module6 中 __all__定义的变量(a,c,d,f)
from subpackage.module6 import *

print(module1.module_name)
# print(subpackage.module3.module_name)
print(module3.module_name)
print(module4_name)
print(module5.module_name)
print(module5_name)
