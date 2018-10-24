from heapq import *
# time limit error
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if len(nums) == 1:
            return [nums[0]*1.0]
        even = 0
        if k % 2 == 0:
            even = 1
        max_heap = []
        min_heap = []
        result = []
        for i in range(len(nums)):
            if len(min_heap) > 0 and nums[i] > min_heap[0]:
                heappush(min_heap, nums[i])
            else:
                heappush(max_heap, -nums[i])
            if len(max_heap) - len(min_heap) > 1:
                heappush(min_heap, -heappop(max_heap))
            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))
            if i >= k - 1:
                result.append((min_heap[0] - max_heap[0]) / 2.0 if even == 1 else float((-max_heap[0])))
                remove = nums[i - k + 1]
                if remove <= -max_heap[0]:
                    max_heap.pop(max_heap.index(-remove))
                    heapify(max_heap)
                else:
                    min_heap.pop(min_heap.index(remove))
                    heapify(min_heap)
                if len(max_heap) - len(min_heap) > 1:
                    heappush(min_heap, -heappop(max_heap))
                if len(min_heap) > len(max_heap):
                    heappush(max_heap, -heappop(min_heap))
        return result

# solution 2
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = sorted(nums[:k-1])
        result = []
        for i in range(k-1, len(nums)):
            bisect.insort(window, nums[i])
            result.append((window[k/2] + window[~(k/2)])/2.0)
            window.remove(nums[i-k+1])
        return result