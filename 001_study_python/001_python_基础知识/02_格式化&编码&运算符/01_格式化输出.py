# -*- encoding:utf-8 -*-
'''
    格式化输出
'''
name = "ll"
age = 24
height = 193

msg = "i am %s, now i am %d old, height %d" % (name, age, height)

print("hello %s this is %%"%name)

'''
    while else循环
    如果while循环不被打断就会执行else的内容
'''
count = 0
while count <= 5:
    count += 1
    if count == 3:
        break
    print('loop', count)
else:
    print('循环正常运行')
print('out of while loop')

