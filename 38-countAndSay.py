import re
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            temp = re.findall(r'((.)\2*)', s)
            s = ''.join(str(len(g)) + char for g,char in temp)
        return s