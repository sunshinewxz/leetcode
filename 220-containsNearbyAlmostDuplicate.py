class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
 
        num_dict = collections.OrderedDict()
        for i in range(len(nums)):
            key = nums[i]//max(t,1)
            for j in (key-1, key, key+1):
                if j in num_dict and abs(nums[i] - num_dict[j]) <= t:
                    print(nums[i])
                    print(num_dict[j])
                    return True
            num_dict[key] = nums[i]
            if i - k >= 0:
                num_dict.popitem(last = False)
        return False
                
                    