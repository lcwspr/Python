'''
    dict : dic = {'name':'lcwspr'}
    增加：
        dic['age'] = 21   没有增加，存在就覆盖
        dic.setdefault()  没有就增加，有不改变

    删除
        pop(key, None)       按照键值删除，有返回值
        clear()
        del dic['name']
        popitem()   随机删除

    改
        update()

    查
        dic.keys()
        dic.values()
        dic.items()

        for k, v in dic.items():
            print(k, v)

        dic.get(key, None)

'''

# 有如下值 li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]，将所有大于66的值保存至字典的第一个key中，将大于66的值保存至第二个key的值中

li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
resMap = {}
resMap['k1'] = []
resMap['k2'] = []
for i in li:
    if i > 66:
        resMap['k1'].append(i)
    elif i < 66:
        resMap['k2'].append(i)
print(resMap)

# 输出商品列表，用户输入序号，显示用户选中的商品
# 商品 li = ['手机', '电脑', '鼠标垫', '游艇']

# 要求： 1： 页面显示 序号 + 商品名称， 如：
#           1 手机
#           2 电脑
#           ...

#       2 用户输入选择的商品序号，然后打印商品名称
#       3 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
#       4 用户输入Q或者q，退出程序

li = ['手机', '电脑', '鼠标垫', '游艇']

flag = True
while flag:
    for i in li:
        print('%d + %s' % (li.index(i) + 1, i))

    num = input('请输入商品序号')

    if num.isdigit():
        num = int(num)

        if num > 0 and num <= len(li):
            print(li[num - 1])
        else:
            print('商品不存在，请重新输入')
            continue

    else:
        print('请输入数字')
        continue

    res = input('输入Q退出程序,回车继续')

    if res.upper() == 'Q':
        flag = False
else:
    print('good bye')
