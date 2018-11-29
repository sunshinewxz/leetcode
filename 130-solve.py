class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        border = []
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                border.append([0,i])
            if board[-1][i] == 'O':
                border.append([len(board)-1, i])
        for i in range(len(board)):
            if board[i][0] == 'O':
                border.append([i,0])
            if board[i][-1] == 'O':
                border.append([i, len(board[0])-1])
        while(len(border) > 0):
            x,y = border.pop()
            if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == 'O':
                board[x][y] = 'D'
                border.append([x-1, y])
                border.append([x+1, y])
                border.append([x, y-1])
                border.append([x, y+1])
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'D':
                    board[x][y] = 'O'
        
        