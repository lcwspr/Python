def qq(l = []):
    l.append(1)
    print(l)

qq()
qq()
qq()
qq([])
qq()

# 注意 如果默认参数是一个可变数据类型
# 那么每一次函数调用时，如果不传值就共用这个数据类型的资源


# 对于字典来说
def showDic(k, l = {}):
    l[k] = 'v'
    print(l)

showDic(1)
showDic(2)
showDic(3)