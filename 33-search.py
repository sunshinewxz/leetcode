class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums)-1
        while(start < end):
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[end]:
                if target in nums[mid:end+1]:
                    start = mid+1
                else:
                    end = mid-1
            elif nums[mid] > nums[end]:
                if target in nums[start:mid+1]:
                    end = mid
                else:
                    start = mid+1
            else:
                end = mid-1
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1

s = Solution()
print(s.search([4,5,6,7,0,1,2],3))
