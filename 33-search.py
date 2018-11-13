class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while(start <= end):
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[end]:
                if nums[mid] < target <= nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            elif nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
        return -1
                    
                    