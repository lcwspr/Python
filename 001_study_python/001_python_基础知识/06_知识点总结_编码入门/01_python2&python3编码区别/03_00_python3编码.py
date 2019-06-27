'''
    编码的演变历史，
    utf-8是如何一步步发展而来的?
    windows为什么还是要保持gbk编码?
'''

# first test
import sys, locale
s = '小甲'
print(s, type(s))
print(sys.getdefaultencoding()) # 值python解释器本身的编码
print(locale.getdefaultlocale()) # 操作系统的本地编码

with open("test_file/utf-8_01", 'w', encoding= 'utf-8') as f:
    f.write(s)
with open("test_file/gbk_01", 'w', encoding= 'gbk') as f:
    f.write(s)
with open("test_file/jis1_01", 'w', encoding= 'shift-jis') as f:
    f.write(s)

