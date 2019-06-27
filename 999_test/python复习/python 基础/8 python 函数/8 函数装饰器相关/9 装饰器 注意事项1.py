"""
    装饰器的叠加
        从上到下去装饰
        从下到上去执行



"""







def zhuangshiqi_line(func):
    def inner():
        print("____________________")
        func()
    return  inner

def zhuangshiqi_star(func):
    def inner():
        print("*"*30)
        func()
    return  inner


@zhuangshiqi_line   # print_content = zhuangshiqi_line(print_content)
@zhuangshiqi_star   # print_content = zhuangshiqi_star(print_content)
def print_content():
    print("社会我顺哥 人很话不多")



print_content()