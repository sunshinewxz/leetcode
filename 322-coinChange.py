class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_n = float('inf')
        dp = [max_n] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            dp[i] = min([dp[i-c] if i >= c else max_n for c in coins]) + 1
        
        if dp[amount] == max_n:
            return -1
        return dp[amount]
        
    