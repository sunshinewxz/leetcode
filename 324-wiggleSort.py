class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        median = self.findMedian(nums, len(nums)//2+1)
        print(median)
        i, j, k = 0, 0, len(nums) - 1
        while(j <= k):
            if nums[j] > median:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] < median:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                i += 1
            else:
                j += 1
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
    
    
    def findMedian(self, nums, k):
        pivot = random.choice(nums)
        less = [i for i in nums[:] if i < pivot]
        larger = [i for i in nums[:] if i > pivot]
        if len(less) >= k:
            return self.findMedian(less, k)
        elif len(nums) - len(larger) < k:
            return self.findMedian(larger, k-(len(nums) - len(larger)))
        return pivot
