class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        result = int((2*n) ** 0.5 -1)
        sum_ = (1+result) * result * 0.5
        while(sum_ <= n):
            result += 1
            sum_ = (1+result) * result * 0.5
        return result-1