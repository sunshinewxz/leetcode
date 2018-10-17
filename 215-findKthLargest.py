# solution 1: sort O(nlogn)
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         if len(nums)==0:
#             return
#         result = nums[0]
#         nums.sort()
#         return nums[len(nums)-k]

# solution 2: quick selection O(n)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for i in range(len(nums)):
            if nums[i] > pivot:
                nums1.append(nums[i])
            elif nums[i] < pivot:
                nums2.append(nums[i])

        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        elif k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums)-len(nums2)))
        return pivot