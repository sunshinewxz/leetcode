class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        depth = 1
        cur_stack = [beginWord]
        next_stack = []
        num = 1
        if beginWord == endWord:
            return 1
        wordList = set(wordList)
        while(len(cur_stack) != 0):
            for word in cur_stack:
                for i in range(len(word)):
                    for c in 'abcdefghigklmnopqrstuvwxyz':
                        word_ = word[0:i]+c+word[i+1:len(word)]
                        if word_ in wordList:
                            next_stack.append(word_)
                            wordList.remove(word_)
                            if word_ == endWord:
                                return depth+1
            cur_stack = next_stack
            next_stack = []
            depth += 1
            # print(depth)
        return 0

            
            