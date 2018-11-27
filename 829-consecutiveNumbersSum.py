class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = 0
        for d in range(1, N+1):
            diff = d * (d-1) / 2
            nd = N - diff
            if nd <= 0:
                break
            if nd % d == 0:
                result += 1
        return result