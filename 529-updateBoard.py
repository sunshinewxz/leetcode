class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click[0], click[1]
        return self.dfs(board, x, y)
        
    def dfs(self, board, x, y):
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        if board[x][y] == 'E':
            mine_num = 0
            for dx,dy in zip([0,0,1,1,1,-1,-1,-1],[1,-1,-1,0,1,-1,0,1]):
                if 0 <= x+dx < len(board) and 0 <= y+dy < len(board[0]) and board[x+dx][y+dy] == 'M':
                    mine_num += 1
            if mine_num == 0:
                board[x][y] = 'B'
                for dx,dy in zip([0,0,1,1,1,-1,-1,-1],[1,-1,-1,0,1,-1,0,1]):
                    if 0 <= x+dx < len(board) and 0 <= y+dy < len(board[0]):
                        self.dfs(board, x+dx, y+dy)
            else:
                board[x][y] = str(mine_num)
        return board