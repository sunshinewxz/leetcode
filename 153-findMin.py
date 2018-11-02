class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        start = 0
        end = len(nums)
        mid = (start + end) // 2
        if nums[mid] < nums[end-1]:
            return self.findMin(nums[:mid+1])
        elif nums[mid] > nums[start]:
            return self.findMin([nums[start]]+nums[mid+1:end])