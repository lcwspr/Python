# -*- coding:utf-8 -*-
# 判断是否是水仙花数

# 1 获取用户输入

for value in range(100, 1000):

    # 2 判断数据有效性
    if not (100 <= value <= 999):
        print('你输入的数据无效 退出程序')
        exit()

    # 求取百位 十位  个位
    water = (value % 10) ** 3 + (value // 10 % 10) ** 3 + (value // 100) ** 3

    if water == value:
        print('你好')
        print("%d 是一个水仙花数" % value)

