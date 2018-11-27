# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def comparePair(a, b):
            return sum(c1 == c2 for c1,c2 in zip(a, b))
        
        def most_overlap():
            count = [[0] * 26 for i in range(6)]
            for word in candidate:
                for i,w in enumerate(word):
                    count[i][ord(w) - ord('a')] += 1
            best_score = 0
            for word in candidate:
                score = 0
                for i,w in enumerate(word):
                    score += count[i][ord(w) - ord('a')]
                if score > best_score:
                    best_score = score
                    best_word = word
            return best_word

        candidate = wordlist[:]
        while(len(candidate) > 0):
            best = most_overlap()
            match_num = master.guess(best)
            if match_num == 6:
                return
            candidate = [c for c in candidate if comparePair(c, best) == match_num]
        
        