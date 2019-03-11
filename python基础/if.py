# print('hello world')

# 流程控制语句
'''
条件控制 循环控制 分支
'''

mood = False

if mood:
    print('go to left')
else:
    print('go to right')

print('back away')

account = 'jeff'
password = '123456'

print("请输入用户名:")
user_account = input()
print("请输入密码:")
user_password = input()

if account == user_account and password == user_password:
    print("登录成功")
else:
    print("用户名或密码错误")
