class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = set(nums)
        sum_all = sum(single) * 2
        return sum_all-sum(nums)