class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        result = []
        multi = False
        line = ''
        for s in source:
        	i = 0
	        while i<len(s):
	        	if not multi:
	        		if s[i] == '/' and i < len(s)-1 and s[i+1] == '/':
	        			break
	        		elif s[i] == '/' and i < len(s)-1 and s[i+1] == '*':
	        			multi = True
	        			i = i + 1
	        		else:
	        			line += s[i]
	        	else:
	        		if s[i] == '*' and i < len(s)-1 and s[i+1] == '/':
	        			multi = False
	        			i = i + 1
	        	i = i + 1
        	if not multi and line:
        		result.append(line)
        		line = ''
        return result

s = Solution()
result = s.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])
print(result)