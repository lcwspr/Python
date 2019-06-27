# 字符串的索引与排序
s = 'ABCDEFGHIJKLMN'
# 索引
s1 = s[0]
print(s1)
s2 = s[2]
print(s2)

# 截取一部分字符串  切片操作，顾头不顾尾
s3 = s[0:4]
print(s3)

# 倒数第几位
s4 = s[-1]
print(s4)

s5 = s[-2]
print(s5)

# 取全部的
s6 = s[0:]
s6 = s[:]   # 一样的写法
# 也就是第一位默认为0  第二位默认为len(str)
print(s6)


# 跳着取子串   s[首:尾:步长]
sstrip = s[:5:2]
print(sstrip)


# 倒着取值
sRev = s[4::-1]
print(sRev)

print(s[-4:-6:-1])

# 永远是从开头:结尾:步长
