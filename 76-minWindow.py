class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_dict = {}
        s_dict = {}
        for i in range(len(t)):
            if t[i] in t_dict:
                t_dict[t[i]] += 1
                s_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1
                s_dict[t[i]] = 1
        start = 0
        count = len(t)
        min_len = len(s)+1
        min_start = 0
        for end in range(len(s)):
            if s[end] in t_dict:
                if t_dict[s[end]] > 0:
                    count -= 1
                t_dict[s[end]] -= 1
            if count == 0:
                while(True):
                    if s[start] in t_dict:
                        if t_dict[s[start]] < 0:
                            t_dict[s[start]] += 1
                        else:
                            break
                    start += 1
                if min_len > end - start + 1:
                    min_len = end - start + 1
                    min_start = start
        if min_len < len(s)+1:
            return s[min_start:min_start+min_len]
        else:
            return ""
                    
                