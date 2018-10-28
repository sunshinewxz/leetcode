class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for i in range(9)] 
        col = [set() for i in range(9)]
        block = [set() for i in range(9)]
        
        for x in range(9):
            for y in range(9):
                if board[x][y] != '.':
                    if board[x][y] in row[x]:
                        return False
                    row[x].add(board[x][y])
                    if board[x][y] in col[y]:
                        return False
                    col[y].add(board[x][y])
                    if board[x][y] in block[(x//3)*3+y//3]:
                        return False
                    block[(x//3)*3+y//3].add(board[x][y])
        return True