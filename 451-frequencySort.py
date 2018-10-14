class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        char_dict = {}
        for i in range(len(s)):
        	if s[i] in char_dict:
        		char_dict[s[i]] = char_dict[s[i]] + 1
        	else:
        		char_dict[s[i]] = 1

        sort_dict = sorted(char_dict.items(), key=lambda d: d[1], reverse=True)
        result = []
        for key_value in sort_dict:
        	result.append("".join([key_value[0]]*key_value[1]))
        result = "".join(result)
        return result

s = Solution()
print(s.frequencySort("tree"))