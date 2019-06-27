"""
    想要加入登录验证
    1 直接在业务逻辑代码去修改 添加验证操作

    缺点
    功能函数重用价值最高   如果我有多个页面 都需要发说说 发图片
    那么每个页面的业务逻辑代码都需要加入
    因为业务逻辑代码非常多 所以  就造成了 每一份 逻辑代码 在调用  具体的功能函数之前 都需要去做一个登录验证   代码冗余度高   代码复用性较差   代码维护性较差

"""
def fss():
    print("发说说")


def ftp():
    print("发图片")


# 相关的逻辑代码
btnIndex = 1
if btnIndex == 1:
    print("登录验证")
    fss()
else:
    print("登录验证")
    ftp()
