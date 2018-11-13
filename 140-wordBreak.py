class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})
        
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return []
        result = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                result.append(word)
            else:
                for restword in self.helper(s[len(word):], wordDict, memo):
                    item = word + ' ' + restword
                    result.append(item)
        memo[s] = result
        return result