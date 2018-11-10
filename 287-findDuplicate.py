class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = sum(nums)
        sum2 = sum(set(nums))
        num_du = len(nums) - len(set(nums))
        return (sum1-sum2)/num_du
    
# solution 2:
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = nums[nums[0]]
        slow = nums[0]
        while(fast != slow):
            fast = nums[nums[fast]]
            slow = nums[slow]
        
        fast = 0
        while(fast != slow):
            fast = nums[fast]
            slow = nums[slow]
        return slow
