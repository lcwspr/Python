# 定义两个功能函数

def fss():
    print("发说说")


def ftp():
    print("发图片")


# 相关的逻辑代码
btnIndex = 1
if btnIndex == 1:
    fss()
else:
    ftp()


# 功能函数 和 业务逻辑代码分离开
# 好处
#     1 帮助我们理清业务逻辑     明确大的业务逻辑
#             关注这个步骤做什么  而不是这个步骤怎么做
#     2 方便代码的重用性
#     3 比较方便代码的维护   改一处就全改了
