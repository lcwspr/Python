"""
    但是还是有一些问题
    违背了开放封闭原则
            已经写好的代码 尽可能不要修改
            如果想要增加新功能  在源代码基础上  单独进行拓展
    单一职责思想



"""


def fss():
    checkLogin()
    print("发说说")


def ftp():
    checkLogin()
    print("发图片")


def checkLogin():
    print("登录验证")


"""

第一种改法

def checkLogin():
    checkLogin()
    print("登录验证")

def checkLogin2():
    checkLogin()
    print("登录验证")

    代码冗余 
    需要修改业务逻辑代码
    不能够写死  
"""

# 相关的逻辑代码
btnIndex = 1
if btnIndex == 1:
    fss()
else:
    ftp()

