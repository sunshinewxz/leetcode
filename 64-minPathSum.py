class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width, height = len(grid[0]), len(grid)
        dp = [0] * width
        dp[0] = grid[0][0]
        for i in range(1, width):
            dp[i] = dp[i-1] + grid[0][i]
        for i in range(1, height):
            for j in range(width):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[width-1]
                    
                