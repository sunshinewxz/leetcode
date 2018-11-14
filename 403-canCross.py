import collections
class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        step = collections.defaultdict(set)
        step[0] = set([1])
        for i in range(len(stones)):
            stone = stones[i]
            for s in step[stone]:
                reach = stone + s
                if reach == stones[-1]:
                    return True
                step[reach].add(s)
                if s-1 > 0:
                    step[reach].add(s-1)
                step[reach].add(s+1)
        return False
                
            