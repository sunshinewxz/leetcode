class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_dict = {}
        for i in range(len(words)):
            word_dict[words[i]] = i
        result = []
        flag = word_dict.get('',-1)
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                temp = words[i][:j]
                ori = words[i][j:]
                if ori == ori[::-1] and temp[::-1] in word_dict and word_dict[temp[::-1]] != i:
                    result.append([i, word_dict[temp[::-1]]])
                if j!= 0 and ori[::-1] in word_dict and temp == temp[::-1] and word_dict[ori[::-1]] != i:
                    result.append([word_dict[ori[::-1]], i])
                # if words[i] == words[i][::-1] and flag != -1 and [i, flag] not in result:
                #     result.append([i, flag])
        # result = list(set(result))
        return result