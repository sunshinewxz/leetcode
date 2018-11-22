from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(lambda a, b: [1,-1][a+b>b+a]))
        result = "".join(nums)
        result = result.lstrip('0') or '0'
        return result