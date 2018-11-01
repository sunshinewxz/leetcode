class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        id_ = {}
        for i in range(n):
            id_[i] = i
            
        def findParents(id):
            if id_[id] == id:
                return id
            while(id != id_[id]):
                id_[id] = id_[id_[id]]
                id = id_[id]
            return id
        count = n
        for link in edges:
            p1 = findParents(link[0])
            p2 = findParents(link[1])
            if p1 != p2:
                id_[p2] = p1
                count -= 1
        return count