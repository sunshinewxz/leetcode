class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        trie = collections.defaultdict(list)
        length = len(words[0])
        for w in words:
            for i in range(length):
                trie[w[:i]].append(w)
        
        def backtrack(square):
            if len(square) == length:
                result.append(square)
                return
            pre = "".join([a[len(square)] for a in square])
            for word in trie[pre]:
                backtrack(square + [word])
            
        result = []
        for w in words:
            backtrack([w])
        return result