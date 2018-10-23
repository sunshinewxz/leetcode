from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        sliding_win = deque()
        result = []
        for i in range(len(nums)):
            if len(sliding_win)>0 and i-sliding_win[0] > k-1:
                sliding_win.popleft()
            if len(sliding_win) > 0 and nums[i] > nums[sliding_win[-1]]:
                while(len(sliding_win)>0 and nums[i]>nums[sliding_win[-1]]):
                    sliding_win.pop()
            sliding_win.append(i)
            if i >= k-1:
                result.append(nums[sliding_win[0]])
        return result
            