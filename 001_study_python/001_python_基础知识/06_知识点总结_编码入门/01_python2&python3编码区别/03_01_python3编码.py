# -*- encoding:gbk -*-
import sys, locale

s = '小甲'

print(s, type(s))
print(sys.getdefaultencoding()) # 值python解释器本身的编码
print(locale.getdefaultlocale()) # 操作系统的本地编码


with open("test_file/utf-8_02", 'w', encoding= 'utf-8') as f:
    f.write(s)
with open("test_file/gbk_02", 'w', encoding= 'gbk') as f:
    f.write(s)
with open("test_file/jis1_02", 'w', encoding= 'shift-jis') as f:
    f.write(s)

'''
    虽然出不来效果，但是是pycharm自动更改文件编码导致
    
    其实头部声明的意思是，python解释器在读取该.py文件的时候，我们应该使用什么格式将其'解码'，只和读取有关，所以当你确定你代码编辑时候的编码，才能够把相应的编码格式写入头文件
    如果文件默认编码为utf-8，而指示解释器使用gbk解码，那么一定会乱码
    
    所以，写了这个头声明，并不会更改本地编码、系统默认编码。
    本地默认编码与操作系统有关，系统默认编码与解释器版本有关
'''

"""
    系统默认编码指的是
        1. 如果Python解释器读取py文件，没有头编码声明，则默认使用系统编码解码
        2. 并且在调用encode() 函数是，不传参数，默认为系统编码
    
    本地默认编码指的是
        1. 在编写Python程序时，若使用了open函数，而不传入encoding，那么会使用本地默认编码
"""

"""
    上面的例子，utf-8文件使用gbk读取之后，写入文件的结果
    utf2:  乱码
    gbk2:  小甲
    jis2:  
    
    问题： 为什么用utf-8去编码存储，后来用utf-8解码取乱码？
    问题： 为什么用gbk去编码存储，后面用Linux默认的'utf-8'去解码，却能够显示
    
    过程   utf-8的乱码  ***怎么来的
    
    小甲(unicode)       ----------用utf-8编码 ----------  e5b0 8fe7 94b2 (u8二进制码)
    e5b0 8fe7 94b2     ----------用gbk解码 ------------  "***" （unicode）乱码
    "***"(unicode)乱码  ----------用gbk编码 ------------  e5b0 8fe7 94b2 （2的逆向）
    e5b0 8fe7 94b2     ----------用utf-8解码 -----------  小甲(unicode)
"""

'''
    解码解错了还能改，在编码回去就好了
'''




s = 'abc中国'
print(repr(s))
print(s.encode('unicode-escape'))

t = b'\\u53eb\\u6211'

print(t.decode('unicode-escape'))
