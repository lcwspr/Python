# -*- coding:utf-8 -*-
# 练习打印1-100 之间的偶数

# 1 首先要有一个1-100的集合
# 一个函数 range(x,y)   可以生成一个列表 从结尾开始  递增+1 生成一个列表 （包含首部元素 不包含尾部）

for num in range(1, 101):
    if num % 3 == 0:
        print(num)
