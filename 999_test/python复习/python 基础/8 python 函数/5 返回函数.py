"""

    概念  是指一个函数内部 他返回的数据是另外一个函数   把这样的操作称为“返回函数”
    案例  根据不同参数   获取不同操作   做不同运算

"""

def getFunc(flag):
    # 1 再次定义几个函数
    def sum(a, b, c):
        return a + b + c

    def sub(a, b):
        return a - b

    # 2 根据不同的flag值  来返回不同的操作函数
    if flag == "+":
        return sum
    elif flag == "-":
        return sub


result = getFunc("+")
print(result, type(result))


