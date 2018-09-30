from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
        	return -1
        dicti = OrderedDict()
        for cha in s:
        	if dicti.__contains__(cha):
        		dicti[cha] += 1
        	else:
        		dicti[cha] = 1
        print(dicti)
        try:
        	result =  s.find(list(dicti.keys())[list(dicti.values()).index(1)])
        	# print(result)
        except ValueError:
        	return -1
        return result

# solution 2
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mini = 2**31 - 1
        cands = "abcdefghijklmnopqrstuvwxyz"
        for c in cands:
            lf = s.find(c)
            rf = s.rfind(c)
            if lf != -1 and lf == rf and lf < mini:
                mini = lf
        return mini if mini != 2**31 - 1 else -1

s = Solution()
result = s.firstUniqChar("dddccdbba")
print(result)