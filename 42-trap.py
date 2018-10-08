class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_most_high = []
        left_most_high.append(height[0])
        most_high = height[0]
        for i in range(1, len(height)):
            if height[i] >= left_most_high[i-1]:
                most_high = height[i]
                left_most_high.append(height[i])
            else:
                left_most_high.append(most_high)
        print(left_most_high)

        water = 0
        right_most = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            if height[i] > right_most:
                right_most = height[i]
            water += min(right_most, left_most_high[i]) - height[i]
            print(water)
        return water

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
