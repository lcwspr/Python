"""
    直接在功能函数里面进行修改  方便代码的重用

    缺点
        但是   登录验证可能由很多代码  代码是不是有重复了？   代码可维护性降低
        继续改进


"""



def fss():
    print("登录验证")
    print("发说说")


def ftp():
    print("登录验证")
    print("发图片")


# 相关的逻辑代码
btnIndex = 1
if btnIndex == 1:
    fss()
else:
    ftp()
