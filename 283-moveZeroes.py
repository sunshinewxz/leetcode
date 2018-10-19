class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        zero_p = 0
        nzero_p = 0
        while(zero_p < len(nums) and nzero_p < len(nums)):
            if nums[zero_p] != 0:
                zero_p += 1
            if nums[nzero_p] == 0:
                nzero_p += 1
            elif nzero_p > zero_p:
                temp = nums[nzero_p]
                nums[nzero_p] = nums[zero_p]
                nums[zero_p] = temp
                nzero_p += 1
                zero_p += 1
            elif nzero_p < zero_p:
                nzero_p += 1

# solution 2
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        currentIndex = 0
        for i in range(len(nums)):
            currentItem = nums[i]
            if currentItem != 0 and i == currentIndex:
                currentIndex += 1
            elif currentItem != 0 and i > currentIndex:
                nums[currentIndex] = currentItem
                currentIndex += 1
                nums[i] = 0
            