class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        line_area = [0 for i in range(len(matrix[0]))]
        result = 0
        # line_area = matrix[0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    line_area[j] = int(matrix[0][j])
                else:
                    line_area[j] = int(matrix[i][j]) + line_area[j] if int(matrix[i][j]) != 0 else 0
            result = max(result, self.largestRectangleArea(line_area))
        return result

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
inpu = [
  ["1",'0']
  # ["1","0","1","1","1"],
  # ["1","1","1","1","1"],
  # ["1","0","0","1","0"]
]
print(s.maximalRectangle(inpu))

