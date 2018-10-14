class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        amount1 = self.singleRob(nums[0:len(nums)-1])
        amount2 = self.singleRob(nums[1:len(nums)])
        return max(amount1, amount2)

    def singleRob(self, nums):
        if len(nums)==0:
            return 0
        amount = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 1:
                amount[i] = max(nums[i-1], nums[i])
            elif i > 1:
                amount[i] = max(amount[i-1], nums[i] + amount[i-2])
            else:
                amount[i] += nums[i]
        return max(amount)

s = Solution()
print(s.rob([2,3,2]))
