class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        def getParent(i):
            if parent[i] != i:
                parent[i] = getParent(parent[i])
            return parent[i]
        id = 0
        count = 0
        result = []
        for x,y in positions:
            parent[(x,y)] = parent[id] = id
            count += 1
            for x_, y_ in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
                if (x_,y_) in parent:
                    q = getParent(parent[(x_, y_)])
                    if q != id:
                        count -= 1
                        parent[q] = id
            id += 1
            result.append(count)
        return result