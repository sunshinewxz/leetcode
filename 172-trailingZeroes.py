class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
        	return 0
        return int(n/5) + self.trailingZeroes(int(n/5))

s = Solution()
print(s.trailingZeroes(30))
