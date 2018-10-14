class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        amount = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 1:
                amount[i] = max(nums[i-1], nums[i])
            elif i > 1:
                amount[i] = max(amount[i-1], nums[i] + amount[i-2])
                print(amount[i])
            else:
                amount[i] += nums[i]
        print(amount)
        return max(amount)

s = Solution()
print(s.rob([2,7,9,3,1]))
