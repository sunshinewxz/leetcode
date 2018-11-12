import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        release1, release2 = 0, 0
        hold1, hold2 = -sys.maxint, -sys.maxint
        for i,p in enumerate(prices):
            release2 = max(release2, hold2+p)
            hold2 = max(hold2, release1-p)
            release1 = max(release1, hold1+p)
            hold1 = max(hold1, -p)
        return release2