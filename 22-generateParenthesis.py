class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        new_str = '('*n+')'*n
        result = [new_str]
        self.bt(new_str, result)
        return result
    
    def bt(self, ori_str, result):
        num = len(ori_str)
        left = 0
        right = 0
        for i in range(num):
            if ori_str[i] == '(':
                left += 1
            elif ori_str[i] == ')':
                right += 1
                if left > right and ori_str[i-1] == '(':
                    new_str = ori_str[0:i-1]+')('+ori_str[i+1:len(ori_str)]
                    if new_str not in result:
                        result.append(new_str)
                        self.bt(new_str, result)
        return result
                    
                    
# solution 2
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate(n, n, "", res)
        return res
        
    
    def generate(self, left, right, str, res):
        if left == 0 and right == 0:
            res.append(str)
            return
        if left > 0:
            self.generate(left - 1, right, str + '(', res)
        if right > left:
            self.generate(left, right - 1, str + ')', res)
