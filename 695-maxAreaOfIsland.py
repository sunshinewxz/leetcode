class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """ 
        max_area = 0
        area = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    max_area = max(max_area, self.dfs(grid, x, y))
        return max_area
        
        
    def dfs(self, grid, x, y):
        if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1 or grid[x][y] == 0:
            return 0
        area = 1
        grid[x][y] = 0
        for dx, dy in zip([0,0,1,-1],[1,-1,0,0]):
            area += self.dfs(grid, x+dx, y+dy)
        return area