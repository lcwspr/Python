"""
    递归函数
        体现
                函数A内部  继续调用函数A
        概念    传递  回归

    注意事项
    案例



"""


# 递归求取阶乘
# 功能  如果是不直接知道结果的数据 就进行分解  (递归调用)
#       如果是知道结果的数据 就直接返回


def get_num(num):
    if num < 0:
        print("error")
    elif num <= 1:
        return 1
    else:
        return num * get_num(num - 1)


l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


def toHex(num, scale):
    if num == 0:
        return 0
    else:
        target = num % scale
        toHex(num // scale, scale)
        print(l[target], end='')


toHex(-88, 2)
