class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0
        stack = []
        heights.append(-1)
        for i in range(len(heights)):
            if len(stack) == 0 or heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while(len(stack) != 0 and heights[i] <= heights[stack[-1]]):
                    h = heights[stack.pop()]
                    w = i if len(stack) == 0 else (i - (stack[-1] + 1))
                    result = max(result, h*w)
                stack.append(i)
        return result

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
