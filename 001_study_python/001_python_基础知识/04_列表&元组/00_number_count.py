
targer = input('please input a string >>> ')

def getCount(str):
    inWord = False
    count = 0

    for x in str:
        if x.isdigit():
            if not inWord:
                inWord = True
                count += 1
        if x.isalpha():
            if inWord:
                inWord = False
    return count

num = getCount(targer)
print(num)