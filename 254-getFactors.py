class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def backtrack(temp, update, first):
            if update != n:
                result.append(temp+[update])
            for num in range(first, int(update**0.5)+1):
                if update % num == 0:
                    backtrack(temp+[num], update//num, num)
            
        result = []
        backtrack([], n, 2)
        return result