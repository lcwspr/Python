# 自定义迭代器
for i in range(9):
    print(i)

class MyRange():

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop -1:
            raise StopIteration
        n = self.start
        self.start  += 1

        return n

lis = MyRange(0, 10)
for i in lis:
    print(i)  # 0 1 2 3 4 5 6 7 8 9
# 迭代器
# 有一些Python对象，我们可以从中按照一定的次序提取出其中的元素，这些对象称之为可迭代对象，比如，字符串，列表，元组等等
# 我们回忆一下从可迭代对象中提取元素的过程，我们显式的使用列表的下标

mystr = 'abc'
for i,_ in enumerate(mystr):
    print(mystr[i])
# 同样一下使用下标进行改写
mylist = [1, 2, 3]
for i,_ in enumerate(mylist):
    mylist[i] += 1
print(mylist)
# 上述中读取和写入，都是通过list的操作符[]实现的，下标只是参数出现，我们把这种模式称之为[可迭代对象是一等公民]
# 那么能不能将下标作为一等公民？换句话说元素的提取之和下标打交道？而与可迭代对象无关，这样的设计模式就是迭代器模式，那个升级版的下标，就是迭代器

# 迭代器模式特别适合
    # 不关心元素的随机访问
    # 元素的个数不可提前预测
my_list = [1, 2, 3]
i = iter(my_list)
while True:
    try:
        print(next(i))
    except StopIteration:
        break
# 一旦迭代器对象建立起来之后，提取元素的过程就不在依赖于原始的可迭代对象，而是仅仅依赖于迭代器本身，python内置的next()函数作用域迭代器会执行三个操作
    # 1. 返回当前位置的元素
    # 2. 将位置向后递增
    # 3. 如果到达可迭代对象的末尾，即没有元素可以提取抛出StopIteration异常
# 也就是说，for语句隐藏了大量的细节

# 使用迭代器的好处
'''
    最大优点在于，能够及时处理未知的事件，(例如用户的输入，网络上的信号)
    并在迭代的过程中随时可以终止迭代。
    例如使用迭代器，我们如果想要生成尽可能多的数据，那么使用迭代器的方法，在每一次迭代之前都检查剩余内存决定是否继续迭代
'''



































