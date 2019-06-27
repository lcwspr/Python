# r+  读写模式
f = open('read&write/log.txt', mode='r+',encoding='utf-8')
print(f.read())
f.write('你好呀，我叫lcwspr')
# 光标最开始位于文件的开始，

# r+  读写模式
f = open('read&write/r+b.txt', mode='r+b')
print(f.read().decode('utf-8'))
f.write('安佳佳姐'.encode('utf-8'))
# 光标最开始位于文件的开始，
# 最常用的就是r+


# w+
f = open('read&write/w+.txt', mode='w+',encoding='utf-8')
f.write('你好呀，我叫lcwspr')
f.seek(0)
con = f.read()
print(con)



# w+b