class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(numchoice, temp):
            if len(temp) == k:
                result.append(temp)
                return
            if len(numchoice) == 0 or len(temp) > k:
                return
            for i,n in enumerate(numchoice):
                temp.append(n)
                backtrack(numchoice[i+1:], temp[:])
                temp.pop()
        backtrack(range(1,n+1), [])
        return result