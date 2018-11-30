class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for n in nums:
            if n in dict:
                return True
            dict[n] = 1
        return False