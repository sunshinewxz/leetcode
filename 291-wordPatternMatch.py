class Solution:
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.backtrack(pattern, str, {})
    
    def backtrack(self, pattern, input_str, dict):
        if len(pattern) == 0 and len(input_str) > 0:
            return False
        if len(pattern) == 0 and len(input_str) == 0:
            return True
        for end in range(1, len(input_str)-len(pattern)+2):
            if pattern[0] not in dict and input_str[:end] not in dict.values():
                dict[pattern[0]] = input_str[:end]
                if self.backtrack(pattern[1:], input_str[end:], dict):
                    return True
                del dict[pattern[0]]
            elif pattern[0] in dict and dict[pattern[0]] == input_str[:end]:
                if self.backtrack(pattern[1:], input_str[end:], dict):
                    return True
        return False