class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1
        return 3**((n-2)//3) * ((n-2)%3 + 2)