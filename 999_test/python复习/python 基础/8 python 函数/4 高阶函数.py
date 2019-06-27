"""

    a， b  形参  ， 2 变量
    传递数据   就是指   给变量赋值
    def test(a, b):
        print(a + b)

    其实函数名也是一个变量名
    开辟空间    将函数体拷贝到内存出  键地址赋给 2 变量

    函数本身也可以作为数据   传递给一个变量


    概念   当一个函数A的参数  接受的又是另一个函数时   则把这个函数A称为高阶函数
    例如   sorted 函数
    案例   动态的计算两个数据
    比较列表中的字典



"""

l = [{"name": "sz", "age": 28}, {"name": "sz2", "age": 48}, {"name": "se", "age": 14}]

def getKey(x):
    return x["age"]


resule = sorted(l, key=getKey)
print(resule)



# 动态计算两个数据
def caculate(num1, num2, caculateFunc):
    print(caculate(num1, num2))


def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

