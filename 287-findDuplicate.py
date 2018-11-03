class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = sum(nums)
        sum2 = sum(set(nums))
        num_du = len(nums) - len(set(nums))
        return (sum1-sum2)/num_du