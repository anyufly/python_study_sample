# 使用dict代替switch
day = 8

day_name_dict = {
    0: 'Sunday',
    1: 'Sonday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
}

day_name = day_name_dict.get(day, 'Unknow')
print(day_name)

season = 5


def get_spring():
    return 'Spring'


def get_summer():
    return 'Summer'


def get_autumn():
    return 'Autumn'


def get_winter():
    return 'Winter'


def get_default():
    return 'Unknow'

season_name_dict = {
    0: get_spring,
    1: get_summer,
    2: get_autumn,
    3: get_winter
}

season_name = season_name_dict.get(season, get_default)()
print(season_name)
