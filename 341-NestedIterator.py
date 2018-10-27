# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.i = []
        self.v = []
        def getList(nestedList):
            for i in range(len(nestedList)):
                if nestedList[i].isInteger():
                    self.i.append(nestedList[i])
                else:
                    getList(nestedList[i].getList())
        getList(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.i.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.i) > 0:
            return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())