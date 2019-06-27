# -*- coding:utf-8 -*-


# 1准备数据
# 1 程序内部定义一个数值 来用来给用户猜测
num = 500
count = 0

while True:

    count += 1
    # 2 数据处理
    # 2.1 让用户输入一个数值
    result = input("请输入一个数字")
    result = int(result)

    # 2.1 拿用户输入的数值与给定数组比较

    # 2.1.1 如果相等  给出正确提示   退出程序
    if result == num:
        print("恭喜你 答对了  答案就是：", result)
        break

    # 2.1.1 如果不相等
    # 2.1.1.1 根据数值关系  给出不同的提示

    # 2.1.1.1.1如果大于  提示 你猜的太大了 小一点
    if result > num:
        print("你猜的太大了  请小一点")

    # 如果小于 。。。。
    else:
        print(" 你猜的太小了  请大一点")

# 让用户继续猜
print("次数为 ", count)
