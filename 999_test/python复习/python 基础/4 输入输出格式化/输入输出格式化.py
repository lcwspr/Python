# _*_ coding:utf-8 _*_

"""
    python 的输入 输出
    运算符的作用是为了处理数据

    数据的获取方式有
        1 程序内部写死的
        2 从文件里面读取
        3 从网络服务器进行获取
        4 接收用户输入

    数据的输出方式有
        1 写回到文件里面保存
        2 发送回服务器
        3 打印到控制台 通过一些界面 展示给用户看



        输入
        Python2

            raw_input()
                格式： result = raw_input("提示信息")

                功能：
                会等待用户输入内容 直到用户按下Enter键
                会将用户输入的内容当做"字符串" 传递给接受的变量


            input()
                格式： result = input('提示信息')

                功能：
                会等待用户输入内容 ，直到用户按下enter键
                会将用户输入的内容当做“代码”进行处理

                可以理解为
                        input = raw_input  +   eval



        python3

            input()
                相当于Python2 中的raw_input
                格式：
                    result = input("提示信息")

                功能：
                    会等待用户输入内容 直到用户按下Enter键
                    会将用户输入的内容当做"字符串" 传递给接受的变量

                如果想要实现类似于Python2 中的input功能
                可以使用eval()函数 来实现



"""
import sys

"""
    
    python 的输出
        python2
            print语句  print xxx
            
            
        python3
            print()函数
                print(values, sep, end, file, flush)
                values  需要输出的值  多个值 使用, 分割开
                sep    分隔符 多个值被输出之后 值与值之间会添加指点分隔符
                end  输出完毕后会以指定的字符结束  默认是换行'\n'
                file 表示输出的目标  默认是控制天  还可以是一个可写入的文件句柄
                flush  表示立即刷新的意思   为bool类型
                
                
"""

"""
# python 2 中

# 1 输出一个值
print 123

# 2 输出一个变量
num = 10
print num

# 3 输出多个变量
num1 = 11
print num, num1

# 4 格式化输出
name = "sz"
age = 18
# 第一种格式化方式
'''我的名字是XXX,年龄是XXX'''
print "我的名字是", name, ",年龄是", age
# 第二种格式化方式
newStr = "我的名字是%s,年龄是%d" % (name, age)
print newStr
# 第三种格式化方式
str1 = "我的名字是{0}，年龄是{1}".format(name, age)
print str1

# 5 输出到文件
f = open("test.txt", "w")
print >>f, str1

# 6  输出不自动换行
print 1,
print 2,
print 3
print 4,
print

# 7 输出的各个数据，使用分隔符分割

print "a", "-", "b", "-", "c"
print "-".join(["a", "b", "c"])









"""

# python 3 中

# 1 输出一个值
print(123)

# 2 输出一个变量
num = 55
print(num)

# 3 输出多个变量
num2 = 66
print(num, num2)

# 4 格式化输出
name = "sz"
age = 18
# 我的名字是XXX，年龄是XXX
print("我的名字是%s, 年龄是%d" % (name, age))
print("我的名字是{0}, 年龄是{1}".format(name, age))

# 5 输出到文件
# print  >>open("test.txt", "w"),"12345"
f = open("test2.txt", "w")
print('-------------', file=f)

print('hello world', file=sys.stdout)

# 6  输出不自动换行
print('abcdef', end="")
print('hhhh')

# 7 输出的各个数据，使用分隔符分割
print('1', '2', '3', sep='=')

from time import sleep

print('我来晚了 不好意思', end='')

print('我来晚了 不好意思', end='', flush=True)
sleep(5)

# 当缓冲区满或者换行是 刷新缓冲区
# 设置flush 参数为True 指定立即刷新缓冲区


"""
    格式化输出
    name = "sz"
    age = 18
    
    # print("我的名字是%s, 年龄是%d"%(name, age))
    # %[(name)][flags][width][.precision]typecode
    # []: 可以省略
    
    
    (name)
    # 表示， 根据， 制定的名称（key），查找对应的值，格式化到字符串当中
    
    mathScore = 59
    englishScore = 58
    print("我的数学分数是%d,英文分数是：%d"%(mathScore, englishScore))
    print("我的数学分数是%d,英文分数是：%d"%(mathScore, englishScore))
    print("我的数学分数是%(ms)d,英文分数是：%(es)d"%({"es":mathScore,"ma":mathScore}))

"""

mathScore = 59
englishScore = 58
print("我的数学分数是%d,英文分数是：%d" % (mathScore, englishScore))
print("我的数学分数是%d,英文分数是：%d" % (mathScore, englishScore))
print("我的数学分数是%(ms)d,英文分数是：%(es)d" % ({"ms": mathScore, "es": englishScore}))

# 当只有一个变量时 可以省略
print("%d" % mathScore)

# width  表示   占用的宽度
print("%10d" % mathScore)

"""
    占位格式符
        格式： %[(name)][flags][width][.precision]typecode
        使用中括号[]  包含的部分，代表可选
        
        解释
            (name)  用于选择指定的名称对应的值
            flags
                空  表示右对齐
                -   表示左对齐
                空格 ' '为一个空格  表示在正数的左侧填充一个空格，从而与负数对齐
                0 表示使用0填充
            [width]   表示显示宽度
            .precision 表示小数点后精度
            typeCode.....
   
"""

"""
    typeCode
        i/d  将整数 浮点数 转换成十进制表示  并将其格式化到指定位置
        o    将整数转换为   8进制表示   
        x    将整数转换为 十六进制表示
        e    将整数 浮点数  转换为科学计数法 （小写e）
        E    将整数 浮点数 转换为科学计数法   （大写E）
        f/F  将整数  浮点数   转换为浮点表示默认为6位小数
        g    自动调整 整数 浮点数  科学计数法（超过六位用科学计数法）（e）
        g    自动调整 整数 浮点数  科学计数法（超过六位用科学计数法）（E）
        s    获取传入对象的_str_方法的返回值  并将其格式化
        r    获取传入对象的_repr_方法返回值  
        c    整数 将整数转换为unicode对应的值  10进制为0<= x <=1114111      python2  为（0-255）
            如果为一个字符    将字符添加到指定位置
            
        
        当字符串中存在格式化标志是， 需要用%%表示一个百分号
        
        
        注意  Python中  不存在直接将整数转换为二进制的表示方式
        
        
"""

print("%  d" % 10)
