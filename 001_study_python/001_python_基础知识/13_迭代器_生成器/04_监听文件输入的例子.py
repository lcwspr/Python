def tail(filename):
    f = open(filename, mode='r',encoding='utf-8')
    while True:
        line = f.readline()
        if line:
            yield line

g = tail('file.txt')
for i in g:
    if 'python' in i:
        print('***' + i)
