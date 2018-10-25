import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        prio_queue = []
        num_dict = {}
        result = []
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1
        for key in num_dict:
            heapq.heappush(prio_queue, [-num_dict[key], key])
        for i in range(k):
            result.append(heapq.heappop(prio_queue)[1])
        return result