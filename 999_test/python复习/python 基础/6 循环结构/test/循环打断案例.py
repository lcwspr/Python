# -*- coding:utf-8 -*-
# 做一个简单的加法计算器  让用户输入两个数值 输出对应的和  用户如果不退出这个程序 则在输入完毕之后 继续让用户使用   如果中间用户输入的数据有误  则给出错误提示 并从头开始 让用户输入数值

while True:
    # 1 先要读取两个数字

    num1 = float(input('请输入第一个数字'))
    num2 = float(input('请输入第二个数字'))

    # 2 判断数字是否满足条件
    if not 1 < num1 <= 100 or not 1 < num2 <= 100:
        print('请输入符合范围的数字')
        continue

    # 3 将两个数字相加  并输出结果
    ss = num1 + num2
    print(ss)

    # 4 判断用户是否还想要继续使用
    flag = input("请输入'q'来表示是否还想要继续输入")
    if flag == 'q':
        break
