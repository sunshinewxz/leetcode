class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        for i,n in enumerate(nums):
            memo[n] = memo.get(n, 0) + 1
        for k in memo.keys():
            if memo[k] > len(nums)/2:
                return k