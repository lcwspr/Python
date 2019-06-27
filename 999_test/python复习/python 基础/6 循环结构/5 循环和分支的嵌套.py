# 循环和分值的嵌套   打印1-100之间所有3的倍数
"""
    循环内嵌套循环
            外循环循环一次   内循环循环所有

"""

for x in range(1, 100):
    if x % 3 == 0:
        print(x)



# 循环中嵌套循环
for i in range(1,6):
    for j in range(1, 3):
        print(j)