import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        num = 1
        self.container = []
        temp = 0
        for w_ in w:
            temp += w_
            self.container.append(temp)
        self.maxint = temp
            
    def pickIndex(self):
        """
        :rtype: int
        """
        rand = random.randint(1,self.maxint)
        index = bisect.bisect_left(self.container, rand)
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()