'''
    给定一个排序数组，你需要在原地删除重复出现的元素，
    使得每个元素只出现一次，返回移除后数组的新长度

    不要使用额外的数组空间，
    你必须在原地修改输入数组并在使用O(1)额外空间的条件下完成
'''
'''
    示例
    给定一个数组 nums = [1, 1, 2]
    函数应该返回新长度2， 并且原数组nums的前两个元素被修改为1， 2
    
    不需要考虑数组中超出新长度后面的元素
'''
'''
    给定nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    函数应该返回新的长度5， 
    并且原数组nums的前5个元素被修改为  0， 1， 2， 3， 4
    
    不需要考虑数组中超出新长度后面的元素
'''


def test(func: 'function') -> None:
    nums = [0, 0, 1, 3, 1, 2, 3, 2, 3, 3, 4, 5]
    func(nums)
    res = []
    for i in nums:
        res.append(i)
    print(res)


# 错误解法 1
def removeDuplicates1(nums: 'list') -> int:
    for num in nums:
        if nums.count(num) > 1:
            nums.remove(num)
    return len(nums)


'''
    使用for发起的任何形式的遍历时，他的遍历顺序都是从最初就确定的，
    而在遍历中删除了元素会导致当前索引的变化，
        1是会导致漏删元素
        2是会导致遍历超过列表的长度
'''

'''
[0, 0, 1, 3, 1, 2, 3, 2, 3, 3, 4, 5]  0
[0, 1, 3, 1, 2, 3, 2, 3, 3, 4, 5]     1
[0, 3, 1, 2, 3, 2, 3, 3, 4, 5]        2
[0, 3, 1, 2, 3, 2, 3, 3, 4, 5]        3
[0, 3, 1, 3, 2, 3, 3, 4, 5]           4
[0, 3, 1, 3, 2, 3, 3, 4, 5]           5
[0, 1, 3, 2, 3, 3, 4, 5]              6
[0, 1, 3, 2, 3, 3, 4, 5]              7
[0, 1, 3, 2, 3, 3, 4, 5]              8
异常终止
'''
# test01
test(removeDuplicates1)


def removeDuplicates2(nums: 'list') -> int:
    '''
    始终创建一个列表的副本，让您可以修改原始的内容
    :param nums:
    :return:
    '''
    for num in nums[:]:
        if num in nums[:]:
            if nums.count(num) > 1:
                nums.remove(num)
    return len(nums)
test(removeDuplicates2)

