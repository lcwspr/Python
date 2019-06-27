'''
ASCII
python在设计的初期绝对没有想到会如此有道欢迎，也没有想到计算机的发展如此迅速，Python最初设计的时候是不需要关心编码的，因为英语的世界里，字符个数非常有限，26个英文字符（大小写），10个数字，标点符号，控制字符，加起来不过100多个字符。一个字节绰绰有余，这就是ascii编码。初代的ascii编码只用了7位，最高位都为0

EASCII
当计算机普及西欧，发现很多字符ASCII编码表中没有，所以拓展出四ASCII编码为EASCII，把原来的七位拓展为8位，兼容与ASCII，但是eascii阶段是一个混乱的阶段，没有统一的标准，

'''



print('昊天'.decode('utf-8'))
print(repr('昊天'))
print(u'hello' + ' yuan')
# print(u'昊天'+'牛逼')  # UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)
'''
    UnicodeError 代码中包含了unicode和bytes字符串，只有数据全部是ASCII，所有转换都是正确的，一旦一个非ASCII字符混入，那么默认解码将会失败
    py2掩盖了从bytes到unicode的过程，但处理非ascii编码会失败
'''

u = u'昊天'
print(repr(u))

s = u.encode('utf-8')
print(repr(s))
print(s)



























