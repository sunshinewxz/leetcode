import collections


class Solution(object):
	def shortestSubarray(self, A, K):
		"""
        :type A: List[int]
        :type K: int
        :rtype: int
        """
		sum_dict = {}
		sum_temp = 0
		sum_dict[0] = 0
		length = len(A) + 1
		for i in range(1, len(A) + 1):
			sum_temp += A[i - 1]
			sum_dict[i] = sum_temp
		queue = collections.deque()

		for i in range(len(A) + 1):
			print(queue)
			while (queue and sum_dict[queue[-1]] >= sum_dict[i]):
				queue.pop()
			while (queue and sum_dict[i] - sum_dict[queue[0]] >= K):
				length = min(length, i - queue.popleft())
			queue.append(i)
		if length > len(A):
			length = -1
		return length


s = Solution()
print(s.shortestSubarray([2, -1, 2], 3))
# print(s.shortestSubarray([1], 1))
# print(s.shortestSubarray([1, 2], 4))