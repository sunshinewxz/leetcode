class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        onum, xnum = 0, 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                onum += 1 if board[i][j] == 'O' else 0
                xnum += 1 if board[i][j] == 'X' else 0
        if onum > xnum:
            return False
        if xnum - onum > 1:
            return False
        if self.isWin(board, 'O') and (xnum != onum or self.isWin(board, 'X')):
            return False
        if self.isWin(board, 'X') and xnum != onum + 1:
            return False
        return True
        
    def isWin(self, board, char):
        for i in range(len(board)):
            if board[i] == char * 3:
                return True
        for i in range(len(board[0])):
            if board[0][i] == char and board[1][i] == char and board[2][i] == char:
                return True
        if (board[0][0] == char and board[1][1] == char and board[2][2] == char) or (board[0][2] == char and board[1][1] == char and board[2][0] == char):
            return True
        return False
        