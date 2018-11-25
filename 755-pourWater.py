class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for i in range(V):
            index = -1
            for j in range(K-1, -1, -1):
                if heights[j] > heights[j+1]:
                    break
                elif heights[j] < heights[j+1]:
                    index = j
            if index != -1:
                heights[index] += 1
                continue
            for j in range(K+1, len(heights)):
                if heights[j] > heights[j-1]:
                    break
                elif heights[j] < heights[j-1]:
                    index = j
            if index != -1:
                heights[index] += 1
                continue
            heights[K] += 1
       
        return heights
                