def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    dic = {
        '1':[],
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],
    }

    li = []
    for c in digits:
        li.append(dic[c])

    temp = []
    str = li[0]
    for i in range(1,len(digits)):
        add_list = li[i]
        for add in add_list:
            temp = temp + addLetter(str,add)
        str = temp
        temp = []
    result = str
    return result

def addLetter(original, add):
    re = []
    for i in range(len(original)):
        re = re + [original[i] + add]
    return re

digits = '233'
result = letterCombinations(digits)
print(result)