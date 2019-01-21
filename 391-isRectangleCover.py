# The right answer must satisfy two conditions:
# 1. the large rectangle area should be equal to the sum of small rectangles
# 2. count of all the points should be even, and that of all the four corner points should be one

# Solution 1
class Solution:
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        points = {}
        area = 0
        con = []
        for rec in rectangles:
            points[(rec[0], rec[1])] = points.get((rec[0], rec[1]), 0) + 1
            points[(rec[2], rec[3])] = points.get((rec[2], rec[3]), 0) + 1
            points[(rec[0], rec[3])] = points.get((rec[0], rec[3]), 0) + 1
            points[(rec[2], rec[1])] = points.get((rec[2], rec[1]), 0) + 1
            area += (rec[2]-rec[0]) * (rec[3] - rec[1])
        temp = []
        for p in points:
            if points[p] == 1:
                temp.append(p)
            elif points[p] % 2 != 0:
                return False
        if len(temp) != 4:
            return False
        area_t = (max(temp[0][0], temp[1][0], temp[2][0], temp[3][0]) - min(temp[0][0], temp[1][0], temp[2][0], temp[3][0])) * (max(temp[0][1], temp[1][1], temp[2][1], temp[3][1]) - min(temp[0][1], temp[1][1], temp[2][1], temp[3][1]))
        if area_t != area:
            return False
        return True

# Solution 2: optimization
class Solution:
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        corners = set()
        area = 0
        
        for x1, y1, x2, y2 in rectangles:
            area += (y2 - y1) * (x2 - x1)
            corners ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
        
        if len(corners) != 4:
            return False
        
        corners = sorted(corners, key=lambda point: (point[0], point[1]))

        if (corners[3][0] - corners[1][0]) * (corners[3][1] - corners[2][1]) != area:
            return False
        return True