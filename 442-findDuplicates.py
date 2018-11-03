class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for n in nums:
            indicator = abs(n) - 1
            if nums[indicator] < 0:
                result.append(abs(n))
            else:
                nums[indicator] = -nums[indicator]
        return result