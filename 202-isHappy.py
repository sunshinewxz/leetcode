class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict = {}
        while(n not in dict):
            dict[n] = 1
            n = sum([int(i) ** 2 for i in str(n)])
            if n == 1:
                return True
        return False