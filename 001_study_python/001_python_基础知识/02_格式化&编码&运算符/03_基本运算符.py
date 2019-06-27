# 见过的就不写了
'''
    and
    or
    not

    优先级  () > not > and > or
'''
print(2 > 1 and 1 < 4)
print(2 > 1 and 1 < 4 or 2 < 3 and 9 > 6 or 2 < 4 and 3 < 2)

# bool()   其他类型转换为bool
# int()    其他类型转换为int

# 短路运算
print(1 or 2)
print(0 or 2)


print(1 > 2 and 3 or 4 and 3 < 2)
