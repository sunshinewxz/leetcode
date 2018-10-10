class Solution(object):
	# solution 
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
       	sum_dict = {}
       	result = 0
       	sum_temp = 0
       	for n in nums:
       		if sum_temp in sum_dict:
       			sum_dict[sum_temp] = sum_dict[sum_temp] + 1
       		else:
       			sum_dict[sum_temp] = 1
       		sum_temp += n
       		if sum_temp-k in sum_dict:
       			result += sum_dict[sum_temp-k]
       	return result

s = Solution()
print(s.subarraySum([1,2,3], 2))