class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = 0
        while(i<len(S)):
            if S[i] == '#' and i > 0:
                S = S[:i-1]+S[i+1:]
                i -= 1
            elif S[i] == '#' and i == 0:
                S = S[1:]
            else:
                i += 1
                
        i = 0
        while(i<len(T)):
            if T[i] == '#' and i > 0:
                T = T[:i-1]+T[i+1:]
                i -= 1
            elif T[i] == '#' and i == 0:
                T = T[1:]
            else:
                i += 1
        return True if S == T else False