def test(func: 'fucntion'):
    test = ['a', '', 'b', '', 'c', '', '']
    func(test)
    print(test)

def showError(nums: 'list'):
    for i in nums:
        if i == '':
            nums.remove(i)

test(showError)

# 发现不能够删除列表中所有的控制，问题如上篇，
# method01
def method01(nums: 'list'):
    while '' in nums:
        nums.remove('')

test(method01)


def method02():
    test = ['a', '', 'b', '', 'c', '', '']
    nums = [x for x in test if x != '']
    print(nums)

method02()