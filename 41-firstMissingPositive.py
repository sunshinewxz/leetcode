class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        length = len(nums)
        for i in range(length):
            if nums[i] < 0 or nums[i] >= length:
                nums[i] = 0
        for i in range(length):
            nums[nums[i]%length] += length
        for i in range(1, length):
            if nums[i]//length == 0:
                return i
        return length
        