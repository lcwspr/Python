# 方法入门
def my_len(s):  # 定义函数，声明函数
    i = 0       # 用于封装重复代码，可以在需要的时候调用
    for k in s:
        i += 1
    print(i)

my_len('hello') # 函数调用

# 返回值  3中情况
    # 没有返回值
        # 不写return
        # 只写return ：
        # return None
    # 返回1个值
        # 可以返回任何类型，返回了就可以接收
        # 多个return只执行第一个
    # 返回多个值
        # 逗号分隔
        # 其实得到的值是一个元组

def a():
    return 1, 2, 3, 4

t = a()
print(t)





















