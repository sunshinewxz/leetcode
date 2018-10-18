class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return[]
        dict = {'1':[], '2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], 
                '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        result = dict[digits[0]]
        for i in range(1, len(digits)):
            result = self.subCombination(result, dict[digits[i]])
        return result
            
    def subCombination(self, list1, list2):
        result = []
        for i in range(len(list1)):
            temp = list1[i]
            for j in range(len(list2)):
                result.append(temp+list2[j])
        return result