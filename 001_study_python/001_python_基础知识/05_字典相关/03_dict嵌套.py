dic = {
    'name': ['first', 'second', 'three'],
    'py':{
        'time': '1214',
        'learn_money': 20000,
        'addr': 'CBD'
    },
    'age': 32
}
print(dic)

dic['age'] = 56
print(dic)

dic['name'].append('hello world')
print(dic)

dic['name'][1] = dic['name'][1].upper()
print(dic)

dic['py']['family_number'] = 6
print(dic)

info = input('>>>')  #oiefio332jejoie83iehh33jewiojife
for i in info:
    if i.isalpha():
        info = info.replace(i, ' ')
l = info.split()
print(len(l))

