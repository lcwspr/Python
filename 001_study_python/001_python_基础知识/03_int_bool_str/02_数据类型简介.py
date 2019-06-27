# int：  1, 2, 3 用于计算
# bool： True,False,用户判断
# str:  'hello world' '1234'  存储少的数据，便于操作
# list： 列表  [1,2, 3,'password',1234,[1,2,3]]
# tuple：元组(1,2,3,'第三方') ，只读列表
# dict:  字典 {'name':'lcwspr', 'age':16}
# set:   {1,2,4,5,7}

int
# bit_length() 方法
# 转换为二进制所需要的最少位数
s = 8
print(s.bit_length())


bool
# True  False

# int ----> str
num = 30
s = str(num)
print(s, type(s))

# str ----> int
s = '1234'
i = int(s)
print(i, type(i))

# int ----> bool   非0就是True
i = 3
b = bool(i)
print(b, type(b))

# bool ----> int
b = True
i = int(b)
print(i, type(i))

# str ---->bool
s = ''
print(bool(s))
s = ' '
print(bool(s))

# bool ----> str
s = True
tr = str(s)
print(tr, type(tr))