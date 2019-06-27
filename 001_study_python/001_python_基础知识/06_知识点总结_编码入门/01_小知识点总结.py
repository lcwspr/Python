"""
1. 区别
    python2
        1. 有print函数和print语句
        2. range()   xrange() 生成器
        3. input()   raw_input()

    python3
        1. 只有print函数
        2. range()
        3. input()
"""

'''
2. 比较
    =  赋值
    == 比较值是否相等
    is 比较地址是否相等，使用的是id()函数
'''
li1 = [1, 2, 3]
li2 = li1
print(li1 is li2)

'''
数字，字符串

会创建数据缓冲区
    数字(-5 -- 256)
    字符串：
        1. 不能含有特殊字符
        2. s *20还是同一个地址， 21就是两个地址(只是用*号运算符)
'''
i1 = 6
i2 = 6
print(id(i1), id(i2))

i3 = 30000
i4 = 30000
print(id(i3), id(i4))

'''
剩下的list dict  tuple set
没有缓冲区的概念
'''


















