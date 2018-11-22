# solution 1
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        temp = [max(nums), min(nums), min(nums)]
        index = 0
        while(index < len(nums)):
            if nums[index] < temp[0] and nums[index] > temp[1]:
                temp[2] = temp[1]
                temp[1] = nums[index]
            elif nums[index] < temp[1] and nums[index] > temp[2]:
                temp[2] = nums[index]
            index += 1
        return temp[2]
                
        

# solution 2
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = None, None, None
        for n in nums:
            if n in [first, second, third]:
                continue
            if first is None or n > first:
                first, second, third = n, first, second
            elif second is None or n > second:
                second, third = n, second
            elif third is None or n > third:
                third = n
        return first if third is None else third