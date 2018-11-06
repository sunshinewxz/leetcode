class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        i, j = 0, len(num) - 1
        maps = [('0','0'), ('1', '1'), ('6', '9'), ('9', '6'), ('8', '8')]
        while(i <= j):
            if (num[i], num[j]) not in maps:
                return False
            i += 1
            j -= 1
        return True
            