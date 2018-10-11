class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        self.district(nums, target, result, 0)
        if len(result) == 0:
            result = [-1, -1]
        if len(result) == 1:
            result.append(result[0])
        final_result = [min(result), max(result)]
        return final_result


    def district(self, nums, target, result, index):
        if len(nums) == 0:
            return
        if len(nums) == 1 and nums[0] == target:
            result.append(index)
            return

        mid = len(nums) // 2
        if nums[mid] > target:
            self.district(nums[0:mid], target, result, index)
        elif nums[mid] < target:
            self.district(nums[mid + 1:len(nums)], target, result, index + mid + 1)
        else:
            if (mid > 0 and nums[mid - 1] < target) or mid == 0:
                result.append(index + mid)
                self.district(nums[mid + 1:len(nums)], target, result, index + mid + 1)
            if (mid < len(nums) - 1 and nums[mid + 1] > target) or mid == len(nums) - 1:
                result.append(index + mid)
                self.district(nums[0:mid], target, result, index)
            self.district(nums[0:mid], target, result, index)
            self.district(nums[mid + 1:len(nums)], target, result, index + mid + 1)

s = Solution()
print(s.searchRange([1, 2, 3, 3, 3, 3, 4, 5, 9], 3))
# print(s.shortestSubarray([1], 1))
# print(s.shortestSubarray([1, 2], 4))