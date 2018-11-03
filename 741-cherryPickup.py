class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.memo = {}
        self.N = len(grid)
        return max(0, self.dp(0,0,0,0))
        
        
    def dp(self, i1, j1, i2, j2):
        if (i1,j1,i2,j2) in self.memo:
            return self.memo[(i1,j1,i2,j2)]
        if i1==self.N-1 and j1==self.N-1 and i2==self.N-1 and j2==self.N-1:
            return self.grid[-1][-1]
        if i1>self.N-1 or j1>self.N-1 or i2>self.N-1 or j2>self.N-1:
            return -1
        if self.grid[i1][j1] == -1 or self.grid[i2][j2] == -1:
            return -1
        dd = self.dp(i1+1, j1, i2+1, j2)
        dr = self.dp(i1+1, j1, i2, j2+1)
        rd = self.dp(i1, j1+1, i2+1, j2)
        rr = self.dp(i1, j1+1, i2, j2+1)
        max_n = max(dd, dr, rd, rr)
        if max_n == -1:
            out = -1
        else:
            if i1==i2 and j1==j2:
                out = max_n + self.grid[i1][j1]
            else:
                out = max_n + self.grid[i1][j1] + self.grid[i2][j2]
        self.memo[(i1,j1,i2,j2)] = out
        return out