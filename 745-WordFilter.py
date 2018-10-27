class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.fix = {}
        for index, word in enumerate(words):
            prefix = ''
            for char in ['']+list(word):
                prefix += char
                suffix = ''
                for schar in ['']+list(word[::-1]):
                    suffix += schar
                    self.fix[prefix + '.' + suffix[::-1]] = index
        # print(self.fix)
    
    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.fix.get(prefix+'.'+suffix, -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)