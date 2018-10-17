class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        result = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - buy_price > result:
                result = prices[i] - buy_price
            if buy_price > prices[i]:
                buy_price = prices[i]
        return result
                