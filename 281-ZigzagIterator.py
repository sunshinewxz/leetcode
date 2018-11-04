class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        p1 = p2 = 0
        self.memo = []
        while(p1 < len(v1) and p2 < len(v2)):
            self.memo.append(v1[p1])
            self.memo.append(v2[p2])
            p1 += 1
            p2 += 1
        if p1 < len(v1):
            self.memo += v1[p1:]
        elif p2 < len(v2):
            self.memo += v2[p2:]
        self.index = 0

    def next(self):
        """
        :rtype: int
        """
        result = self.memo[self.index]
        self.index += 1
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index == len(self.memo):
            return False
        return True
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())