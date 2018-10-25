class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        queue = []
        queue.append(s)
        result = []
        num = len(s)+1
        # remove_num = 0
        while(len(queue) > 0):
            s_ori = queue.pop(0)
            if self.judge(s_ori):
                num = len(s_ori)
                if s_ori not in result:
                    result.append(s_ori)
            elif num > len(s):
                for i in range(len(s_ori)):
                    if s_ori[i] == '(' or s_ori[i] == ')':
                        s_up = s_ori[:i]+s_ori[i+1:len(s_ori)]
                        if s_up not in queue:
                            queue.append(s_up)
        if len(result) == 0:
            result.append("")
        return result
                    
        
        
    def judge(self, s):
        temp = 0
        for i in s:
            if i == '(':
                temp += 1
            elif i == ')':
                temp -= 1
            if temp < 0:
                return False
        if temp > 0:
            return False
        return True
    

# dfs and some optimization
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        l, r = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            elif s[i] == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
        self.dfs(r, l, s, result, 0, len(s))
        return result
            
    def judge(self, s):
        temp = 0
        for i in s:
            if i == '(':
                temp += 1
            elif i == ')':
                if temp > 0:
                    temp -= 1
                else:
                    return False
        return True
    
    def dfs(self, r, l, s, result, lstart, rstart):
        if l == r == 0:
            if self.judge(s):
                if s not in result:
                    result.append(s)
                return
        elif r > 0:
            for i in reversed(range(rstart)):
                print(s)
                print(i)
                if s[i] == ')' and (i==len(s)-1 or s[i+1]!=')'):
                    self.dfs(r-1, l, s[:i]+s[i+1:], result, lstart, i)
        elif l > 0:
            for i in range(lstart, len(s)):
                if s[i] == '(' and (i==0 or s[i-1]!='('):
                    self.dfs(r, l-1, s[:i]+s[i+1:], result, i, rstart)
        return result
        