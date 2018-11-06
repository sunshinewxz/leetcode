class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width, height = len(grid[0]), len(grid)
        hit = [[0] * width for i in range(height)]
        distance = [[0] * width for i in range(height)]
        building_num = sum(val for line in grid for val in line if val == 1)
        
        def bfs(startx, starty):
            visited = [[False] * width for i in range(height)]
            visited[startx][starty] = True
            count = 1
            queue = collections.deque([(startx, starty, 0)])
            while(len(queue) > 0):
                x, y, dis = queue.popleft()
                for dx, dy in zip([0,0,1,-1], [1,-1,0,0]):
                    if 0 <= x+dx < height and 0 <= y+dy < width and not visited[x+dx][y+dy]:
                        visited[x+dx][y+dy] = True
                        if grid[x+dx][y+dy] == 0:
                            queue.append((x+dx, y+dy, dis+1))
                            hit[x+dx][y+dy] += 1
                            distance[x+dx][y+dy] += dis + 1
                        elif grid[x+dx][y+dy] == 1:
                            count += 1
            return count == building_num
            
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    if not bfs(i, j):
                        return -1
        
        return min([distance[i][j] for i in range(height) for j in range(width) if hit[i][j] == building_num and grid[i][j] == 0] or [-1])