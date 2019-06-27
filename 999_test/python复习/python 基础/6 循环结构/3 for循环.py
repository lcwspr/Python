"""
    使用场景  重复性的执行一些操作  更多的是遍历一个集合

    一般使用
        语法
            for x in xxx:
                循环语句

        解释
            xxx 通常是一个集合
            x 会取出集合中的每一个元素 赋值给变量x
            在循环体中  可以直接使用x的值
            当集合中的元素被遍历完毕后 循环就会结束



    与else连用

    语法
        for x in xxx:
            条件满足时执行的代码
        else:
            条件不满足时执行的语句

    注意
        如果for循环可以顺利的执行完毕则会执行else
        反之   使用了break则不会



"""

# 遍历一个集合

str1 = '我叫你爸爸  你说狠不狠'
for x in str1:
    print(x, end='')
    break
else:
    print("\r\n集合遍历结束")

# 翻转字符串
str2 = '我叫你爸爸  你说狠不狠'
# 首先要先拆开字符串

# 定义一个变量倒叙加
newStr = ""
for x in str1:
    newStr = x + newStr
print(newStr)

# 打印1-100的偶数

for x in range(1, 101):
    if x % 2 == 0:
        print("%d 是偶数" % x)
