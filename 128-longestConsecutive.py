from heapq import *
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        heap = []
        for n in nums:
            heappush(heap, n)
        result = 0
        temp = []
        while(len(heap) > 0):
            first = heappop(heap)
            if len(temp) > 0:
                if first == temp[-1]:
                    result = max(result, len(temp))
                    continue
                if first-temp[-1] == 1:
                    temp.append(first)
                    result = max(result, len(temp))
                else:
                    result = max(result, len(temp))
                    temp = [first]
            else:
                temp.append(first)
        return result

# solution 2:
class Solution:
    def longestConsecutive(self, nums):
        mp = set(nums)
        result = 0
        for num in mp:
            if num-1 not in mp:
                count = 1
                while num+count in mp:
                    count+=1
                result = max(result,count)      
        return result