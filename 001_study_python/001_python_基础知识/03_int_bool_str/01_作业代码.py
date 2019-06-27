# 计算 1 - 2 + 3 ... + 99 除了88 意外数其他所有数的和

nowNum = 0
sum = 0

while nowNum < 99:
    nowNum += 1
    if nowNum % 2:
        sum += nowNum
    else:
        if nowNum == 88:
            continue
        sum -= nowNum
print(sum)

# 计算 1 - 2 + 3 ... - 99 中除了88意外数之外所有数的总和

sign = -1
now = 0
sum = 0

while now < 99:
    now += 1
    if now != 88:
        sign = -sign
    else:
        continue
    sum += sign * now

print(sum)

# 用户登录(三次输错机会)且每次输入错误的时候显示剩余错误次数   使用字符串格式化

ps = '12345'
count = 3
while count > 0:
    passWord = input('请输入用户密码')
    count -= 1

    if ps == passWord:
        print('恭喜，登录成功')
        break
    else:
        print('请重新尝试  还有%d机会'%count)

print('bey')