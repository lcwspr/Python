"""
    于是 将 登录验证操作 封装成函数
    功能得到了重用 可维护性增高
    


"""

def fss():
    checkLogin()
    print("发说说")


def ftp():
    checkLogin()
    print("发图片")


def checkLogin():
    print("登录验证")


# 相关的逻辑代码
btnIndex = 1
if btnIndex == 1:
    fss()
else:
    ftp()
