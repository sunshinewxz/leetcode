class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        temp = nums[0] + nums[1] + nums[2]
        result = temp
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while(left < right):
                temp = nums[i] + nums[left] + nums[right]
                if temp == target:
                    return temp
                if abs(temp-target) < abs(result-target):
                    result = temp
                if temp - target > 0:
                    right -= 1
                elif temp - target < 0:
                    left += 1
        return result
            