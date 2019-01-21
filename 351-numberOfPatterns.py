class Solution:
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def backtrack(cur, remain):
            num = 0
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            visit[cur-1] = True
            for i in range(1,10):
                if visit[i-1] == False:
                    first = min(cur, i)
                    second = max(cur, i)
                    if ((first, second) in skip and visit[skip[(first, second)]-1]) or (first, second) not in skip:
                        num += backtrack(i, remain-1)
            visit[cur-1] = False
            return num

        skip = {}
        skip[(1, 3)] = 2
        skip[(4, 6)] = 5
        skip[(7, 9)] = 8
        skip[(1, 7)] = 4
        skip[(2, 8)] = 5
        skip[(3, 9)] = 6
        skip[(1, 9)] = 5
        skip[(3, 7)] = 5
        skip[(2, 8)] = 5
        skip[(4, 6)] = 5
        
        result = 0
        visit = [False] * 9
        for r in range(m-1,n):
            result += backtrack(1, r) * 4
            result += backtrack(2, r) * 4
            result += backtrack(5, r)
        
        return result
        