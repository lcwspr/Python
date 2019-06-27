# -*- encoding:utf-8 -*-

u'''
    什么是字符编码?
    我们从一段信息说起来，我们从一段信息说起，消息以人类可读的易懂的表示方式我们称为明文
        从明文到编码文本的转换称为编码
        从编码文本转回明文则称为解码
'''

u'''
    py2编码
    str & unicode  都是basestring的子类
    
    str是字节串，他是unicode经过编码后的字节组成的序列
    所以str '腕' 使用len函数时结果是3
    
    unicode是一个字符串，str是这个字符串经过编码后的字节组成的序列
    unicode才是真正意义上的字符串，对于字节串使用正确的编码解码获得    
'''

u'''
        py2中   str == bytes
        py2最大的特点是py2会自动将bytes数据解码成unicode字符串
        所以可以将字节与字符串拼接
'''



# python 3
"""
    Python3 也有两种类型，一个是unicode 一个是byte但是有不同的命名
    
    普通类型转换为str后存储的是unicode,byte类型存储的是byte
    
    python3中最大的特点要属于对于文本和二进制数据做了更为清晰地区分
    文本总是由unicode来表示，二进制数据总是由bytes表示。
    python3不会使用任何方式混用他们（所以不能拼接字符串和字节串）
"""



