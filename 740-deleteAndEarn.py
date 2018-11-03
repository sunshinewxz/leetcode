import collections
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = collections.Counter(nums)
        count = sorted(count.items())
        dp = [0, count[0][0]*count[0][1]]
        for i in range(1, len(count)):
            if count[i][0]-count[i-1][0] == 1:
                temp0 = dp[0] + count[i][1]*count[i][0]
                dp[0] = dp[1]
                dp[1] = max(temp0, dp[1])
            else:
                dp[0] = dp[1]
                dp[1] += count[i][1]*count[i][0]
        return dp[1]
        