'''
    ascii
        一个字符占8位

    unicode
        16/32(python 3都是32位)

    utf-8
        ascii相关编码占用8位
        中文相关编码占用24位

    gbk
        ascii相关编码占用8位
        中文相关编码占用16位

'''
'''
    1. 各个编码之间的二进制，是不能相互识别的，会产生乱码
    2. 文件的存储，传输，不能使unicode(只能是utf-8，utf-16，gbk，gb2312,ascii)
'''
"""
    py3:str在内存中使用的是unicode编码存储的
    
    bytes类型
    
    对于英文
        str : 表现形式: s = 'lcwspr'
              编码方式 01010101100  unicode
        
        bytes : 表现形式： s = b'lcwspr'
              编码方式 01010110100 utf-8 gbk
    
    对于英文
        str : 表现形式: s = '中国'
              编码方式 01010101100  unicode
        
        bytes : 表现形式： s = b'x'
              编码方式 01010110100 utf-8 gbk         
      
"""

s = 'lcwspr'
s1 = b'lcwspr'
s2 = u'lcwspr'

print(s, type(s))
print(s1, type(s1))
print(s2, type(s2))


s = '中国'
s1 = '中国'.encode('gbk')
s2 = u'中国'

print(s, type(s))
print(s1, type(s1))
print(s2, type(s2))
