# -*- encoding:gbk -*-
import sys, locale

s = 'С��'

print(s, type(s))
print(sys.getdefaultencoding()) # ֵpython����������ı���
print(locale.getdefaultlocale()) # ����ϵͳ�ı��ر���


with open("test_file/utf-8_02", 'w', encoding= 'utf-8') as f:
    f.write(s)
with open("test_file/gbk_02", 'w', encoding= 'gbk') as f:
    f.write(s)
with open("test_file/jis1_02", 'w', encoding= 'shift-jis') as f:
    f.write(s)

'''
    ��Ȼ������Ч����������pycharm�Զ������ļ����뵼��
    
    ��ʵͷ����������˼�ǣ�python�������ڶ�ȡ��.py�ļ���ʱ������Ӧ��ʹ��ʲô��ʽ����'����'��ֻ�Ͷ�ȡ�йأ����Ե���ȷ�������༭ʱ��ı��룬���ܹ�����Ӧ�ı����ʽд��ͷ�ļ�
    ����ļ�Ĭ�ϱ���Ϊutf-8����ָʾ������ʹ��gbk���룬��ôһ��������
    
    ���ԣ�д�����ͷ��������������ı��ر��롢ϵͳĬ�ϱ��롣
    ����Ĭ�ϱ��������ϵͳ�йأ�ϵͳĬ�ϱ�����������汾�й�
'''

"""
    ϵͳĬ�ϱ���ָ����
        1. ���Python��������ȡpy�ļ���û��ͷ������������Ĭ��ʹ��ϵͳ�������
        2. �����ڵ���encode() �����ǣ�����������Ĭ��Ϊϵͳ����
    
    ����Ĭ�ϱ���ָ����
        1. �ڱ�дPython����ʱ����ʹ����open��������������encoding����ô��ʹ�ñ���Ĭ�ϱ���
"""

"""
    ��������ӣ�utf-8�ļ�ʹ��gbk��ȡ֮��д���ļ��Ľ��
    utf2:  ����
    gbk2:  С��
    jis2:  
    
    ���⣺ Ϊʲô��utf-8ȥ����洢��������utf-8����ȡ���룿
    ���⣺ Ϊʲô��gbkȥ����洢��������LinuxĬ�ϵ�'utf-8'ȥ���룬ȴ�ܹ���ʾ
    
    ����   utf-8������  ***��ô����
    
    С��(unicode)       ----------��utf-8���� ----------  e5b0 8fe7 94b2 (u8��������)
    e5b0 8fe7 94b2     ----------��gbk���� ------------  "***" ��unicode������
    "***"(unicode)����  ----------��gbk���� ------------  e5b0 8fe7 94b2 ��2������
    e5b0 8fe7 94b2     ----------��utf-8���� -----------  С��(unicode)
"""

'''
    �������˻��ܸģ��ڱ����ȥ�ͺ���
'''




s = 'abc�й�'
print(repr(s))
print(s.encode('unicode-escape'))

t = b'\\u53eb\\u6211'

print(t.decode('unicode-escape'))
