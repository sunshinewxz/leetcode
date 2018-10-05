class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for x in range(len(board)):
            for y in range(len(board[0])):
                result = self.search(board, word, x, y, 0)
                if result:
                    return True
        return False

    def search(self, board, word, x, y, sear_len):
        if sear_len == len(word):
            return True
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        if board[x][y] != word[sear_len]:
            return False
        print(board[x][y])
        board[x][y] = board[x][y].swapcase()

        result = self.search(board, word, x+1, y, sear_len+1) or self.search(board, word, x, y+1, sear_len+1) or self.search(board, word, x-1, y, sear_len+1) or self.search(board, word, x, y-1, sear_len+1)
        board[x][y] = board[x][y].swapcase()
        print(board[x][y])
        return result

s = Solution()
board = [
  ['C','A','A'],
  ['A','A','A'],
  ['B','C','D']
]
print(s.exist(board, "AAB"))  