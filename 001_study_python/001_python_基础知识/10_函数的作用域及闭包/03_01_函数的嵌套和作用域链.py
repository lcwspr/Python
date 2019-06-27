# test01
print('*'*20 + 'test01')
def max(a, b):
    return a if a > b else b

def the_max(x, y, z):  # 函数的嵌套调用
    c = max(x, y)
    return max(c, z)

print(the_max(73, 22, 23))

print('*'*20 + 'test02')

# test02
# 函数的嵌套定义
# 内部函数可以使用外部函数的变量
def outer():
    a = 1
    def inner():
        b = 2
        print(a)
        print('inner1')

        def inner2():
            nonlocal b  # 声明上面一层的局部变量

            print(a, b)
            b += 1
            print('inner2')
        inner2()
    inner()
outer()
# nonlocal 只能用于局部变量，找上层中立当前函数最近一层的局部变量
# 声明了nonlocal的内部函数的变量修改会影响到离当前函数最近一层的局部变量
# 对于全局无效
# 对于局部也只是对于最近的一层有影响

print('*'*20 + 'test03')
# test03
def func():
    print(123)

func()   # 函数名就是内存地址
func2 = func # 函数名可以赋值
func2()

l = [func, func2] # 函数名可以作为容器类型的元素
print(l)
for i in l:
    i()

def test03(f):   # 函数名可以作为函数的参数和返回值
    f()
    return f
test03(func)

# 第一类对象(first-class object)
'''
    1. 可在运行期间创建
    2. 可用作函数参数或者返回值
    3. 可以存入变量的实体(容器类型的元素，可以进行变量的赋值)
'''