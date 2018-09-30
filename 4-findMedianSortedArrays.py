class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1) + len(nums2)) % 2 != 0:
            return self.getKth(nums1, nums2, (len(nums1)+len(nums2))/2+1)
        else:
            return 0.5 * (self.getKth(nums1, nums2, (len(nums1)+len(nums2))/2) + self.getKth(nums1, nums2, (len(nums1)+len(nums2))/2+1))
        
    def getKth(self, A, B, k):
        k = int(k)
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB:
            return self.getKth(B, A, k)
        if lenA == 0:
            return B[k-1]
        if k==1:
            return min(A[0], B[0])
        pa = int(min(k/2, len(A)))
        pb = int(k-pa)
        if A[pa-1] <= B[pb-1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)



s = Solution()
nums1 = [1,2]
nums2 = [3,4]
result = float(s.findMedianSortedArrays(nums1, nums2))
print(result)


