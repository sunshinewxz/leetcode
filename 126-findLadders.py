import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        result = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        wordList = set(wordList)
        while (len(layer)>0):
            new_layer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    result.extend(w for w in layer[word])
                else:
                    for i in range(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in wordList:
                                new_layer[new_word] += [ori+[new_word] for ori in layer[word]]
            wordList -= set(new_layer.keys())
            layer = new_layer
        return result