class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.subSum(nums, 4, target, [], [])
        
        
    def subSum(self, nums, n, target, result, all_result):
        if n == 2:
            l, r = 0, len(nums)-1
            while(l < r):
                mid = (l+r) // 2
                if nums[l] + nums[r] == target:
                    all_result.append(result+[nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while(l < len(nums) and nums[l] == nums[l-1]):
                        l += 1
                    while(r >= 0 and nums[r] == nums[r+1]):
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
        else:
            for i in range(len(nums)-n+1):
                if target < nums[i] * n:
                    break
                if i == 0 or (i>0 and nums[i] != nums[i-1]):
                    self.subSum(nums[i+1:], n-1, target-nums[i], result+[nums[i]], all_result)
        return all_result