class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        width, height = len(board[0]), len(board)
        while(True):
            delete = []
            for i in range(height):
                for j in range(width):
                    if board[i][j] != 0:
                        xmin, xmax, ymin, ymax = i, i, j, j
                        while(xmin >= 0 and xmin > i-3 and board[i][j] == board[xmin][j]):
                            xmin -= 1
                        while(xmax < height and xmax < i+3 and board[i][j] == board[xmax][j]):
                            xmax += 1
                        while(ymin >= 0 and ymin > j-3 and board[i][j] == board[i][ymin]):
                            ymin -= 1
                        while(ymax < width and ymax < j+3 and board[i][j] == board[i][ymax]):
                            ymax += 1
                        if ymax-ymin >= 4 or xmax - xmin >= 4:
                            delete.append([i,j])
            if len(delete) == 0:
                break
            for d in delete:
                board[d[0]][d[1]] = 0
            for j in range(width):
                index = height - 1
                for i in range(height-1,-1,-1):
                    if board[i][j] != 0:
                        temp = board[i][j]
                        board[i][j] = board[index][j]
                        board[index][j] = temp
                        index -= 1
        return board
                    
                        