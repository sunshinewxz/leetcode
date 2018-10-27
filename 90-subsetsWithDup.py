class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(temp, start, end):
            result.append(temp[:])
            for i in range(start, end):
                if i>start and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                backtrack(temp, i+1, end)
                temp.pop()
            
        result = []
        nums = sorted(nums)
        backtrack([], 0, len(nums))
        return result