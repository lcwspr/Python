"""
    循环打断 对else的影响
        如果循环正常执行完毕 则会执行else部分
        如果中途是因为打断而退出循环 则不会执行else部分

    break 打断本次循环 跳出整个循环
    continue 结束本次循环 继续执行下次循环

    练习



"""

""" 
    需求  做一个简单的加法计算器 让用户输入两个数值 输出对应的和
    要求  用户如果不退出知恩阁程序 则输出完毕之后 继续让用户使用
            如果中间用户输入的数据有误  则给出错误提示  并从头开始  让用户输入数值
    

"""
while True:
    print("请输入两个数值来求和")
    num1 = int(input("请输入一个数值"))
    num2 = int(input("请输入第二个数值"))

    if not(0 < num1 < 100 and 0 < num2 <100):
        print("请重新输入0-100的数据")
        continue
    nSum = num1 + num2

    print("当前的运算结果为%d" % nSum)
    flag = input("如需继续运算请输入y")
    if flag != "y":
        break
print("欢迎下次使用")
































