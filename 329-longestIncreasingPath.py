class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        dp = [[0]*len(matrix[0])  for j in range(len(matrix))]
        
        def dfs(x, y):
            for dx, dy in zip([0, 0, 1, -1],[1, -1, 0, 0]):
                if x+dx >= 0 and y+dy >= 0 and x+dx < len(matrix) and y+dy < len(matrix[0]) and matrix[x+dx][y+dy] > matrix[x][y]:
                    if not dp[x+dx][y+dy]:
                        dp[x+dx][y+dy] = dfs(x+dx, y+dy)
                    dp[x][y] = max(dp[x][y], dp[x+dx][y+dy] + 1)
            dp[x][y] = max(dp[x][y], 1)
            return dp[x][y]
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if not dp[x][y]:
                    dp[x][y] = dfs(x, y)

        return max([max(x) for x in dp])