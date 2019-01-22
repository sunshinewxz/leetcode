class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        two_count = {}
        for a in A:
            for b in B:
                two_count[a+b] = two_count.get(a+b, 0) + 1
        
        result = 0
        for c in C:
            for d in D:
                result += two_count.get(-c-d, 0)
        return result
        