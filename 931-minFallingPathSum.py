class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dp = [[0] * len(A[0]) for i in range(len(A))]
        dp[0] = A[0]
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + A[i][j]
                elif j == len(A[0])-1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + A[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + A[i][j]
        return min(dp[len(A)-1])
        