class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
            else:
                for i in range(start, end):
                    nums[i], nums[start] = nums[start], nums[i]
                    backtrack(start+1, end)
                    nums[i], nums[start] = nums[start], nums[i]
        result = []
        backtrack(0, len(nums))
        return result
    
# solution 2
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, result, [])
        return result
        
    def dfs(self, nums, result, temp):
        if len(nums) == 0:
            result.append(temp)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], result, temp+[nums[i]])
            
