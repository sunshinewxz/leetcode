# time limit error
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        pre = {}
        for w in words:
            if w[0] in pre:
                pre[w[0]].append(w)
            else:
                pre[w[0]] = [w]
        print(pre)
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] in pre and pre[board[x][y]] is not None:
                    for word in pre[board[x][y]]:
                        visited = [[0] * len(board[0]) for i in range(len(board))]
                        flag = 0
                        flag = self.dfs(board, word, x, y, visited, flag)
                        if flag == 1:
                            result.append(word)
                            pre[board[x][y]].remove(word)
        return result
        
    def dfs(self, board, word, x, y, visited, flag):
        if len(word) == 0 or flag == 1:
            return 1
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[0] or visited[x][y] == 1:
            return flag
        visited[x][y] = 1
        for dx, dy in zip([0,0,1,-1],[1,-1,0,0]):
            flag = self.dfs(board, word[1:], x+dx, y+dy, visited, flag)
        visited[x][y] = 0
        return flag


# solution 2: trie
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        self.result = set()
        self.visited = [[0] * len(board[0]) for i in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[0])):
                self.dfs(board, x, y, trie, '')
        return list(self.result)
                
    def dfs(self, board, x, y, trie, temp):
        if '#' in trie:
            self.result.add(temp)
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] not in trie or self.visited[x][y] == 1:
            return
        self.visited[x][y] = 1
        for dx, dy in zip([0,0,1,-1],[1,-1,0,0]):
            self.dfs(board, x+dx, y+dy, trie[board[x][y]], temp+board[x][y])
        self.visited[x][y] = 0
            