import bisect
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_dict = {}
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while(len(stack)>0 and nums[i]>stack[-1]):
                stack.pop()
            if len(stack) == 0:
                nums_dict[nums[i]] = -1
            else:
                nums_dict[nums[i]] = stack[-1]
            stack.append(nums[i])
        result = []
        for i in range(len(findNums)):
            result.append(nums_dict[findNums[i]])
        return result
                