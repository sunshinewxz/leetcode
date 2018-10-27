class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = ''
                    path = self.dfs(grid, i, j, path, 's')
                    result.add(path)
                    # print(result)
        return len(result)

    def dfs(self, grid, x, y, path, char):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return path
        grid[x][y] = 0
        path += char
        path = self.dfs(grid, x - 1, y, path, 'u')
        path = self.dfs(grid, x + 1, y, path, 'd')
        path = self.dfs(grid, x, y - 1, path, 'l')
        path = self.dfs(grid, x, y + 1, path, 'r')
        path += 'e'
        # print(path)
        return path