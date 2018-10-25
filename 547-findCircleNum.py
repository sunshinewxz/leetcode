
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        result = 0
        for x in range(len(M)):
            for y in range(len(M[0])):
                if M[x][y] == 1:
                    # M[x][y] = 0
                    result += 1
                    self.dfs(M, x, y)
        return result
        
    def dfs(self, M, x, y):
        if x < 0 or y < 0 or x > len(M)-1 or y > len(M[0]) - 1 or M[x][y] == 0:
            return
        M[x][y] = 0
        for i in range(len(M)):
            if M[i][y] == 1:
                self.dfs(M, i, y)
                M[i][y] = 0
        for i in range(len(M[0])):
            if M[x][i] == 1:
                self.dfs(M, x, i)
                M[x][i] = 0
        return

# solution 2

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(M)):
            result += self.dfs(M, i)
        return result
        
    def dfs(self, M, i):
        flag = 0
        for j in range(len(M)):
            if M[i][j] == 1 or M[j][i] == 1:
                M[i][j] = 0
                M[j][i] = 0
                self.dfs(M, j)
                flag = 1
        return flag
        