class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        length = len(nums) + 1
        sum_temp = 0
        for right in range(len(nums)):
            sum_temp += nums[right]
            if sum_temp >= s:
                while(sum_temp >= s):
                    sum_temp -= nums[left]
                    left += 1
                length = min(length, right-left+2)
        if length > len(nums):
            return 0
        else:
            return length