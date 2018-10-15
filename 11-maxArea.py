class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        start = 0
        end = len(height) - 1
        while(start < end):
            if height[start] < height[end]:
                if height[start] * (end - start) > result:
                    result = height[start] * (end - start)
                start += 1
            else:
                if height[end] * (end - start) > result:
                    result = height[end] * (end - start)
                end -= 1
        return result