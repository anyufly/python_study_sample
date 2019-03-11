from enum import Enum
# 使用IntEnum中的枚举值只能为int, 枚举值为float时会被自动取整
from enum import IntEnum
from enum import unique


# 使用unique装饰器，则枚举内不能定义重复的枚举值
@unique
class VIP(IntEnum):
    YELLOW = 1.2
    # YELLOW = 2
    # 不能定义重复的枚举名称， 不然会报错定义值相等的
    # 定义重复的枚举值，后定义的会看做先定义的枚举类型别名
    # 使用IntEnum中的枚举值只能为int, 枚举值为float时会被自动取整
    # YELLOW_ALIAS = 1.3
    GREEN = 2
    RED = 3.8
    BLACK = 4

print(VIP.GREEN.name)
# 枚举值
print(VIP.GREEN.value)
# 枚举类型
print(type(VIP.GREEN))
# 枚举名称
print(type(VIP.GREEN.name))
# 通过枚举名称访问枚举类型
print(VIP['GREEN'])

# YELLOW:1
# GREEN:2
# RED:3
# BLACK:4
# 直接遍历无法遍历出别名
for v in VIP:
    print(v.name + ':' + str(v.value))

# 遍历别名，需要遍历枚举的__members__内置变量
for v in VIP.__members__:
    print(v)
# VIP.__members__.items() ---> (name, enum_meta)
for name, meta in VIP.__members__.items():
    print(name + ':' + str(meta.value))
# 使用枚举值获取枚举类型
yellow = VIP(1)
# VIP.YELLOW
print(yellow)
