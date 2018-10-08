class Solution(object):
    def __init__(self):
        self.count = 0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [-1 for i in range(n)]
        self.dfs(0, board, n)
        return self.count

    def dfs(self, depth, board, n):
        if depth == n:
            self.count += 1
        for row in range(n):
            if self.check(depth, row, board):
                board[depth] = row
                self.dfs(depth+1, board, n)

    def check(self, depth, row, board):
        for i in range(depth):
            if board[i] == row or abs(depth-i)==abs(board[i]-row):
                return False
        return True

s = Solution()
print(s.totalNQueens(4))
