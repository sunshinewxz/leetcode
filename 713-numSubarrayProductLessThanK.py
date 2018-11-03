class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        result = 0
        mul = 1
        for i in range(len(nums)):
            mul = mul * nums[i]
            while(mul >= k and left<=i):
                mul /= nums[left]
                left += 1
            result += i - left + 1
        return result