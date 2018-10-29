class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sums = [0] * k
        subsum = sum(nums)//k
        l = len(nums)
        nums = sorted(nums, reverse=True)
        
        def search(i):
            # print(i)
            if i >= l:
                return len(set(sums)) == 1
            for j in range(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and search(i+1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    return False
            return False
        return search(0)
                