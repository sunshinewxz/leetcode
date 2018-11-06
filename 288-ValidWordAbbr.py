class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.memo = collections.defaultdict(list)
        for d in dictionary:
            if len(d) > 2:
                first = d[0]
                last = d[-1]
                num = len(d) - 2
                temp = first + str(num) + last
                if d not in self.memo[temp]:
                    self.memo[temp].append(d)
            else:
                if d not in self.memo[d]:
                    self.memo[d].append(d)
        
    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # print(self.memo)
        if len(word) > 2:
            first = word[0]
            last = word[-1]
            num = len(word) - 2
            temp = first + str(num) + last
        else:
            temp = word
        if temp in self.memo and (word not in self.memo[temp] or len(self.memo[temp]) > 1):
            return False
        return True


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)