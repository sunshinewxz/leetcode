class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = list(str(x))
        if temp[0] == '-':
            temp = temp[1:len(temp)]
            temp.reverse()
            num = int("".join(temp))
            if num > 2**31:
                return 0
            else:
                return num*(-1)
        else:
            temp.reverse()
            num = int("".join(temp))
            if num > 2**31-1:
                return 0
            else:
                return num
        