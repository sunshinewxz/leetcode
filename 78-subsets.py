class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result = [[]]
        # for n in nums:
        # 	for r in result[:]:
        # 		temp = r[:]
        # 		temp.append(n)
        # 		result.append(temp)
        # 		print(result)
        # return result

    # solution 2: dfs
    def subsets(self, nums):
        result = []
        self.dfs(nums, 0, 0, [], result)
        return result


    def dfs(self, nums, length, index, curr, result):
        result.append(curr)
        if length == len(nums):
            return
        for i in range(index, len(nums)):
            self.dfs(nums, length+1, i+1, curr+[nums[i]], result)


s = Solution()
print(s.subsets([1, 2, 3]))
