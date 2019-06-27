# 字符串的操作

# 首字母大写
s = 'my name is lcwspr'
print(s.capitalize())

# 全大写，全小写
print("lcwspr".upper())
print("LCWSPR".lower())

# 忽略大小写验证输入
'''
    s_str = 'acEQ1'
    you_input = input('please input')
    if s_str.upper() == you_input.upper():
        print(' good job')
    else:
        print('please test again')
'''

# 大小写翻转
s2 = "MY NAME is lcwspr"
print(s2.swapcase())

# 每个(被特殊字符或者数字隔开)的单词首字母大写
s = 'alex*egon-wusir'
print(s.title())

s = 'fade,crazy*w4rri0r_songsong node_3'
print(s.title())

# 居中，空白填充
s = 'alexWUsir'
print(s.center(20))
print(s.center(20,'~'))

# 拓展空格，指定数目
s = 'alex\tsir'
print(s.expandtabs())

# 求取字符串长度
s = "lcwspr"
print(len(s))

# 以什么开头，结尾
s = "first.txt"
print(s.startswith("first"))
print(s.endswith(".txt"))

# find 通过元素找索引，找不到返回-1
s = "hello world"    # 有切片操作  [字符串,起始,结束]
print('hello world'.find('wo',0,3))
print('hello world'.find('helo'))

# index 通过元素找索引，找不到报错
s = "alexWUsir"
print(s.find('A'))
print(s.index(''))

# strip, rstrip, lstrip  去除两端的空格
s = "     hello world my namei is   "
print("|%s|"%s.strip())
print("|%s|"%s.lstrip())
print("|%s|"%s.rstrip())


s = "%%%  hello world +%"
print(s.strip('%+ '))


# username = input('请输入名字：').strip()
# if username =='jjj':
#     print('恭喜春哥发财')

# count  返回子串在父串中出现的次数  有切片操作
s = 'alexaal wusalirl'
s10 = s.count('al')
print(s10)

# split    str->list
s = ":hello;this;test;good"
print(s.split(';'))


# format的三种玩法 格式化输出
s = '我叫{}，今年{}，爱好{}，再说一下我叫{}'.format('太白',36,'girl','太白')
print(s)

name = 'hello world'
s = '我叫{0}，今年{1}，爱好{2}，再说一下我叫{0}'.format(name,36,'girl')
print(s)

name = 'hello world'
s = '我叫{name}，今年{age}，爱好{hobby}，再说一下我叫{name}'.format(age=18,name=name,hobby='girl')
print(s)

# 替换操作
s = 'hello world this is world , good world'
print(s.replace('world', 'good', 1))

# 判断操作  in     not in
s = 'hello world this is world'
if 'world' in s:
    print('it is in it')









