class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        bucket = {}
        for i,n in enumerate(nums):
            bucket_index = n//t if t > 0 else n
            offset = 1 if t > 0 else 0
            for index in range(bucket_index-offset, bucket_index+offset+1):
                if index in bucket and abs(bucket[index] - n) <= t:
                    return True
            bucket[bucket_index] = n
            if len(bucket) > k:
                del bucket[nums[i-k]//t if t>0 else nums[i-k]]
        return False