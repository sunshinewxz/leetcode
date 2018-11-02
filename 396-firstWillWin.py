class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        min_value = min(values)
        dp = [[None] * len(values) for i in range(len(values))]
        for i in range(len(values)):
            dp[i][i] = values[i]
        for leng in range(1, len(values)):
            for i in range(len(values)-leng):
                j = i + leng
                dp[i][j] = max(values[i] - dp[i+1][j], values[j] - dp[i][j-1])
        print(dp)
        if dp[0][len(values)-1] < 0:
            return False
        return True