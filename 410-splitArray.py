class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def isValid(mid):
            group_num = 0
            curr = 0
            for n in nums:
                curr += n
                if curr > mid:
                    group_num += 1
                    if group_num >= m:
                        return False
                    curr = n
            return True
        
        low, high = max(nums), sum(nums)
        while(low < high):
            mid = low + (high-low) // 2
            if isValid(mid):
                high = mid
            else:
                low = mid+1
        return low