# solution 1: auto-grader only accepts the first(leftmost) correct answer, so this solution can not pass auto-grader.
class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        position = {}
        for i in range(len(flowers)):
            position[flowers[i]] = i
            
        position = sorted(position.items(), key=lambda v:v[0])
        for i in range(0,len(position)-k-1):
            flag = 1
            second_time = position[i+k+1][1]
            t = max(position[i][1], second_time)
            for j in range(i+1,i+k+1):
                if position[j][1] <= t:
                    flag = 0
                    break
            if flag == 1:
                return t+1
        return -1

# solution 2
# time complexity: O(n), space complexity: O(n)
class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        garden = [[i - 1, i + 1] for i in range(len(flowers))]
        garden[0][0], garden[-1][1] = None, None
        ans = -1
        for i in range(len(flowers) - 1, -1, -1):
            cur = flowers[i] - 1
            left, right = garden[cur]
            if right != None and right - cur == k + 1:
                ans = i + 1
            if left != None and cur - left == k + 1:
                ans = i + 1
            if right != None:
                garden[right][0] = left
            if left != None:
                garden[left][1] = right
        return ans