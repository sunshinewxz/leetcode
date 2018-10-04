class Solution:
    def twoSum(self, nums, target):
        numtoindexmap = {}
        for num1_index, num1 in enumerate(nums):
            num2 = target - num1
            try:
                num2_index = numtoindexmap[num2]
            except KeyError:
                numtoindexmap[num1] = num1_index
            else:
                num1_re = min(num1_index, num2_index)
                num2_re= max(num1_index, num2_index)
                return num1_re, num2_re


nums = [3,3]
target = 6
s = Solution()
print(s.twoSum(nums, target))