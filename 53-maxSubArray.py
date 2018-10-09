class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        current = 0
        for i in range(len(nums)):
        	current += nums[i]
        	if current > result:
        		result = current
        	if current < 0:
        		current = 0
        return result


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
