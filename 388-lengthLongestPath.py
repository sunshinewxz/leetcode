class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if len(input) == 0:
            return 0
        stack = []
        result = 0
        for str_ in input.split('\n'):
            while(len(stack) > str_.count('\t')):
                stack.pop()
            if str_.count('.') == 0:
                stack.append(len(str_.strip('\t'))+1)
            else:
                result = max(result, sum(stack)+len(str_.strip('\t')))
        return result
                                