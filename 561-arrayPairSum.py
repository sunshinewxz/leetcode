class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        result = 0
        for i in range(0, len(nums)-1, 2):
            result += min(nums[i], nums[i+1])
        return result