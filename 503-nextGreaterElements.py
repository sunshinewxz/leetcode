class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        stack = []
        nums = nums+nums
        for i in range(len(nums)-1,-1,-1):
            while(len(stack)>0 and nums[i]>=stack[-1]):
                stack.pop()
            index = i%(len(nums)/2)
            # print(index)
            if len(stack) == 0:
                res[index] = -1
            else:
                res[index] = stack[-1]
            stack.append(nums[i])
        return res