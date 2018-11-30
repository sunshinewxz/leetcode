class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        size = 0
        pre = 0
        dp = [0] * (len(matrix)+1)
        for j in range(len(matrix[0])):
            for i in range(1, len(matrix)+1):
                temp = dp[i]
                if matrix[i-1][j] == '1':
                    dp[i] = min(dp[i], dp[i-1], pre) + 1
                    size = max(size, dp[i])
                else:
                    dp[i] = 0
                pre = temp
        return size * size