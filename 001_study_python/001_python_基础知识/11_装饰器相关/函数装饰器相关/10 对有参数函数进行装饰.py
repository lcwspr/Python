"""
    无论什么场景 保证函数调用参数个数一致
    为了通用  可以使用不定长参数  结合拆包操作进行处理

"""
def zsq(func):
    def inner():
        print("_"*30)
        func()
    return inner



def pnum():
    print(10)



pnum()