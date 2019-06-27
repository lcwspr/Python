"""
   语法
        while  条件:
            条件满足时的代码
    执行流程
        先判断条件是否满足
        满足执行   不满足退出
    解释
    练习


    while循环与else连用
        语法
            while 条件:
                条件满足时的语句
            else:
                条件不满足时的语句
    如果通过打断语句  break退出循环不会执行else
    python 中没有do while



"""
# while True:
#     print("hello")

# 打印十遍 helloworld


# while
# 一定要注意 以后写循环的时候 要考虑好 循环的结束
# 修改条件
# 打断循环   break

num = 1
nSum = 0
while num <= 10:
    nSum += num
    num += 1
print(nSum)
