class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def helper(i, j):
            if j > 8:
                i += 1
                j = 0
            if i == 9:
                return True
            if board[i][j] != '.':
                return helper(i, j+1)
            row = set(board[i])
            col = set(board[r][j] for r in range(9))
            h, l = 3*(i//3), 3*(j//3)
            block = set(board[m][n] for m in range(h, h+3) for n in range(l, l+3))
            candidates = set(map(str, range(1,10))) - (row | col | block)
            for c in candidates:
                board[i][j] = c
                if helper(i, j+1):
                    return True
                board[i][j] = '.'
            return False
        helper(0,0)
        return
            