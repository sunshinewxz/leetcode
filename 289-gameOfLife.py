class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.w = len(board)
        self.h = len(board[0])
        for x in range(self.w):
            for y in range(self.h):
                if self.getNeighbor(x, y) == 3 and self.board[x][y] == 0:
                    self.board[x][y] = 3
                elif (self.getNeighbor(x, y) < 2 or self.getNeighbor(x, y) > 3) and self.board[x][y] == 1:
                    self.board[x][y] = 2
        for x in range(self.w):
            for y in range(self.h):
                if board[x][y] == 2:
                    board[x][y] = 0
                elif board[x][y] == 3:
                    board[x][y] = 1
                
    def getNeighbor(self, x, y):
        count = 0
        for dx, dy in zip([-1,-1,-1,0,0,+1,+1,+1],[-1,0,+1,-1,+1,-1,0,+1]):
            if 0<=x+dx<self.w and 0<=y+dy<self.h:
                if 1<= self.board[x+dx][y+dy] <= 2:
                    count += 1
        return count
            