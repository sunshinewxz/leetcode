# solution 1: time limited error
class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [['']*n for i in range(n)]
        self.n = n
        self.win = None

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board[row][col] = 'X' if player == 1 else 'O'
        # print(self.board)
        if self.isWin():
            return self.win
        else:
            return 0
        
    def isWin(self):
        for i in range(self.n):
            if self.board[i] == ['O'] * self.n:
                self.win = 2
                return True
            if self.board[i] == ['X'] * self.n:
                self.win = 1
                return True
        for i in range(self.n):
            temp = [self.board[j][i] for j in range(self.n)]
            # print(temp)
            if temp == ['O']*self.n:
                self.win = 2
                return True
            if temp == ['X']*self.n:
                self.win = 1
                return True
        # for i,j in zip(range(self.n), range(self.n)):
        temp = [self.board[i][j] for i,j in zip(range(self.n), range(self.n))]
        if temp == ['O']*self.n:
            self.win = 2
            return True
        if temp == ['X']*self.n:
            self.win = 1
            return True
        temp = [self.board[i][j] for i,j in zip(range(self.n), range(self.n-1, -1, -1))]
        if temp == ['O']*self.n:
            self.win = 2
            return True
        if temp == ['X']*self.n:
            self.win = 1
            return True


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# solution 2
class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row, self.col, self.diag, self.rediag = [0]*n, [0]*n, 0, 0
        self.n = n
        
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        offset = 2 * player - 3
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row+col == self.n-1:
            self.rediag += offset
        if self.n in[self.row[row], self.col[col], self.diag, self.rediag]:
            return 2
        if -self.n in[self.row[row], self.col[col], self.diag, self.rediag]:
            return 1
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
