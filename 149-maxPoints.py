# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from decimal import *
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        
        result = 0
        for i in range(len(points)-1):
            point_dict = {'i':0}
            same = 0
            temp = 0
            verticle = 1
            for j in range(i+1, len(points)):
                p1_x, p1_y = points[i].x, points[i].y
                p2_x, p2_y = points[j].x, points[j].y
                if p1_x == p2_x and p1_y == p2_y:
                    same += 1
                    continue
                elif p1_x == p2_x:
                    verticle += 1
                    continue
                else:
                    slope = Decimal(p2_y - p1_y)/Decimal(p2_x - p1_x)
                    if slope in point_dict:
                        point_dict[slope] += 1
                    else:
                        point_dict[slope] = 2
                temp = max(max(point_dict.values()), temp)
                
            result = max(result, max(temp, verticle)+same)
        return result
                    