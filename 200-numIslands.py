class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    self.dfs(x, y, grid)
                    result += 1   
        return result

    def dfs(self, dx, dy, grid):
        if dx >= len(grid) or dx < 0 or dy >= len(grid[0]) or dy < 0:
            return 
        if dx - 1 >= 0 and grid[dx-1][dy] == '1':
            grid[dx-1][dy] = '0'
            self.dfs(dx-1, dy, grid)
        if dx + 1 < len(grid) and grid[dx+1][dy] == '1':
            grid[dx+1][dy] = '0'
            self.dfs(dx+1, dy, grid)
        if dy - 1 >= 0 and grid[dx][dy-1] == '1':
            grid[dx][dy-1] = '0'
            self.dfs(dx, dy-1, grid)
        if dy + 1 < len(grid[0]) and grid[dx][dy+1] == '1':
            grid[dx][dy+1] = '0'
            self.dfs(dx, dy+1, grid)


s = Solution()
grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
print(s.numIslands(grid))