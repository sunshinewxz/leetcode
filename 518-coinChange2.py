class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        dp = [0] * (amount+1)
        dp[0] = 1

        for c in coins:
            for amou in range(c, amount+1):
                dp[amou] += dp[amou-c]
        return dp[amount]