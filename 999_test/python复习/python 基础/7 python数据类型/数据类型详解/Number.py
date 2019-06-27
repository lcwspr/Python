"""
    表现形式
    1 整数
        二进制  ob
        八进制  0o
        十进制  不需要加前缀
        十六进制 0x

    2 浮点数（float）
        由整数部分和小数部分组成  168.2
        可以使用科学计数法表示   1.682e2

    3 复数（complex）
        由实部和虚部组成  a+bj  可以complex(a,b)
        a,b 都是浮点数
    注意  Python3的整形  可以自动调整大小 可以当做long类型使用



    进制的概念
        可以理解为进位的制度   逢X进1   就是x进制
    常用的进制为（2  8  10    16）

    3 进制的转换
    其他进制转换为10 进制        基数乘权 相加

    十进制转换为其他进制         规律  乘除倒取余
    函数 bin() 可以将10进制数据转换为二进制数据
    函数oct() 可以将10进制数据转换为8进制数据
    函数hex()  可以将10进制数据转换为16进制数据

    常用操作
        适用于几乎所有Python运算符

        算数运算符
        符合运算符
        比较运算符
        链式比较运算符
        逻辑运算符

            注意  当int和float类型进行判断时  会被提升为float类型

        数学函数
        Python有很多的第三方库
        内建的  自带的
        模块函数  需要导入相应的模块


        导入相应的模块  例如  import math
        使用函数时 模块名.函数名(参数)   例如 math.abs(-10)


        内建函数
            abs()  求一个数的绝对值
            max(num1, num2)  求最大值   可以传入很多参数 也可以传入一个列表
            min(num, num2)   求最小值  上同
            round(num[,n])   求一个值的四舍五入  [，n] 可选表示四舍五入的小数位数
            pow(x, y) 返回 x 的 y次幂  相当于  x**y




        math模块函数   需要导入模块
                    import math    例如： math.ceil()

                ceil()  上取整
                floor() 下取整
                sqrt()  开平方
                log(n, base)  base 为基数



        随机函数   必须要导入随机模块 random

                random()     [0,1)  范围内的随机小数

                choice(seq)   从一个序列中挑选一个数值
                            例如random.choice((1,3,5,6))

                uniform(x, y)   [x, y] 范围内随机的小数

                randint(x, y)  [0, 1] 随机整数

                randrange(start, stop = none, step = 1)
                给定区间内的一随机整数   （start, stop）



        三角函数

                三角函数
            正弦（参数接收是一个弧度值）
            pi = 180
            弧度  = (角度/180) *pi

            sin(x)
            cos(x)
            tan(x)
            asin(x)
            acos(x)
            atan(x)
            degrees(x)
            radians(x)


            数学中的常量 pi


"""
import math
import random

# 内建函数
print(abs(-3))
print(min(34, 56, 23))
print(max(45, 89, 23))
print(pow(3, 7))
print(round(3.4567, 3))

# math 模块函数
print(math.ceil(4.235))
print(math.floor(3.345))
print(math.log(100, 10))
print(math.sqrt(36))

# 1 random
print(random.random())

# 2 choice
print(type(random.choice((3, 78, 67, 23))))

# 3 范围内随机小数 [start, end]
print(random.uniform(2, 7))

# 4 random.randint()    返回范围内整数[start, end]
print(random.randint(3, 9))

# 5 给定区间内的任一随机整数  可以设置增长步长  randrange(start, stop = null, step = 1)    不包括结束

print(random.randrange(0, 4, 2))

# 数学函数  三角相关函数
"""
    三角函数  
    正弦（参数接收是一个弧度值）
    pi = 180
    弧度  = (角度/180) *pi
    
    sin(x)
    cos(x)
    tan(x)
    asin(x)
    acos(x)
    atan(x)
    degrees(x)
    radians(x)

"""

print(math.sin(math.radians(45)))

print(math.pi)
