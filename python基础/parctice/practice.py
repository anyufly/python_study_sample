'''
6级五行石合成划算还是购买划算
'''

# 五行石合成规则：
# 消耗品：金、钻石、体力
# 1个1级石头： 0.75金和8个钻石
# 1级五行石合成3级五行石：消耗0.39金、10体力、1个1级五行石和12个1级五行石
# 3级五行石合成4级五行石：消耗0.897金、10体力、1个3级五行石和16个1级五行石、概率为0.4878
# 如果失败，则金和16颗1级五行石也将被扣除，但是不消耗体力
# 4级五行石合成6级五行石：消耗19.75金、10体力、1个四级五行石和12个4级五行石

# 一颗6级石头750金
# 一颗钻石0.05金
# 1点体力 1金

# 直接购买划算还是合成划算
from random import randint

DIAMOND = 0.05
STRENGTH = 1
LEVEL_SIX_PRICE = 750
COMBINE_RATE = 0.4878


def get_level_one_stone():
    '''
    1个1级石头： 0.75金和8个钻石，一个钻石0.05金
    '''
    return 0.75 + DIAMOND * 8


def get_level_three_stone():
    '''
    1级五行石合成3级五行石：消耗0.39金、10体力、1个1级五行石和12个1级五行石
    '''
    return 0.39 + STRENGTH * 10 + get_level_one_stone() \
        + 12 * get_level_one_stone()


def judge(rate=COMBINE_RATE):
    '''
    合成概率判定
    '''
    points = randint(1, 10000)
    # print('摇出的点数：' + str(points))
    if points > 0 and points <= COMBINE_RATE * 10000:
        return True
    else:
        return False


def combine_level_four_stone(price):
    # 判定成功返回
    if(judge()):
        # print('判定成功')
        price += 0.897 + STRENGTH * 10 + 16 * get_level_one_stone()
        return price
    else:
        # print('判定失败')
        price += 0.897 + 16 * get_level_one_stone()
        return combine_level_four_stone(price)


def get_level_four_stone():
    '''
    3级五行石合成4级五行石：消耗0.897金、10体力、1个3级五行石和16个1级五行石、概率为0.4878
    如果失败，则金和16颗1级五行石也将被扣除，但是不消耗体力
    '''
    price = get_level_three_stone()
    return combine_level_four_stone(price)


def get_level_six_stone():
    '''
    4级五行石合成6级五行石：消耗19.75金、10体力、1个四级五行石和12个4级五行石
    '''
    price = 19.75 + STRENGTH * 10
    for i in range(1, 14):
        price += get_level_four_stone()

    return price


def compare_price():
    '''
    比价格
    '''
    price1 = get_level_six_stone()
    price2 = LEVEL_SIX_PRICE

    print('合成需要' + str(price1) + '金')
    print('购买需要' + str(LEVEL_SIX_PRICE) + '金')

    if price1 < price2:
        print('合成划算')
    elif price1 == price2:
        print('合成或购买价格一样')
    else:
        print('合成不划算')

compare_price()
