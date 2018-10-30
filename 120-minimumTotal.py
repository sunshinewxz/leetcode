class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        layer_num = len(triangle)
        dp = [0] * layer_num
        for i in range(layer_num):
            dp[i] = triangle[layer_num-1][i]
        for i in range(layer_num-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]