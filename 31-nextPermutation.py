class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = len(nums)-1
        while(index > 0 and nums[index]<=nums[index-1]):
            index -= 1
        if index == 0:
            nums.reverse()
        else:
            insert_num = nums[index-1]
            temp = len(nums)-1
            while(nums[temp] <= nums[index-1] and temp != index-1):
                temp -= 1
            nums[index-1], nums[temp] = nums[temp], nums[index-1]
            end = len(nums)-1
            while(index < end):
                nums[index], nums[end] = nums[end], nums[index]
                index += 1
                end -= 1