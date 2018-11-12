# solution 1: memory error
import sys
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
        hold = [-sys.maxint] * k
        release = [0] * k
        for p in prices:
            for i in range(k-1,0,-1):
                release[i] = max(release[i], hold[i]+p)
                hold[i] = max(hold[i], release[i-1]-p)
            release[0] = max(release[0], hold[0]+p)
            hold[0] = max(hold[0], -p)
        return release[-1]

# solution 2
'''
To solve the problem of memory error, we need to decide whether k >= len(prices)/2.
When k >= len(prices)/2, the problem convert to the sell and sold problem II
'''
import sys
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or k == 0:
            return 0
        p_num = len(prices)
        if k >= p_num/2:
            return self.sellbuy2(prices)
        dp = [[0] * p_num for i in range(k+1)]
        for i in range(1,k+1):
            temp = -prices[0]
            for j in range(1, p_num):
                dp[i][j] = max(dp[i][j-1], temp + prices[j])
                temp = max(temp, dp[i-1][j-1]-prices[j])
        return dp[k][p_num-1]
    
    def sellbuy2(self, prices):
        result = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                result += prices[i+1] - prices[i]
        return result