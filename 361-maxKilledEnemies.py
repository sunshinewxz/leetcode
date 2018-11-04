import copy
# time limited error
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    result = max(result, self.dfs(copy.deepcopy(grid), 0, i, j))
        # print(grid)
        return result
        
        
    def dfs(self, grid, result, x, y):
        i = y
        while(i < len(grid[0])):
            if grid[x][i] == 'E':
                result += 1
                grid[x][i] = 'O'
            elif grid[x][i] == 'W':
                break
            i += 1
        i = y
        while(i >= 0):
            if grid[x][i] == 'E':
                result += 1
                grid[x][i] = 'O'
            elif grid[x][i] == 'W':
                break
            i -= 1
        j = x
        while(j < len(grid)):
            if grid[j][y] == 'E':
                result += 1
                grid[j][y] = 'O'
            elif grid[j][y] == 'W':
                break
            j += 1
        j = x
        while(j >= 0):
            if grid[j][y] == 'E':
                result += 1
                grid[j][y] = 'O'
            elif grid[j][y] == 'W':
                break
            j -= 1
        return result


# solution 2:
import copy
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        self.killRows(grid)
        return self.killCols(grid)
        
        
    def killRows(self, grid):
        for i in range(len(grid)):
            zero = []
            enemy = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'W':
                    while(len(zero) > 0):
                        index = zero.pop()
                        grid[i][index] = enemy
                    enemy = 0
                elif grid[i][j] == 'E':
                    enemy += 1
                else:
                    zero.append(j)
            while(len(zero) > 0):
                index = zero.pop()
                grid[i][index] = enemy
                    
    def killCols(self, grid):
        result = 0
        for j in range(len(grid[0])):
            zero = []
            enemy = 0
            for i in range(len(grid)):
                if grid[i][j] == 'W':
                    while(len(zero) > 0):
                        index = zero.pop()
                        grid[index][j] += enemy
                        result = max(result, grid[index][j])
                    enemy = 0
                elif grid[i][j] == 'E':
                    enemy += 1
                else:
                    zero.append(i)
            while(len(zero) > 0):
                index = zero.pop()
                grid[index][j] += enemy
                result = max(result, grid[index][j])
        return result
                    


