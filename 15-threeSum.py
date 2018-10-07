# Time Limit Exceeded
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_dict = {}
        result = []
        nums.sort()

        for x_index in range(len(nums)-2):
            index_yz = self.twoSum(nums[x_index+1:len(nums)], 0-nums[x_index])
            for i in index_yz:
                temp = [nums[x_index]] + [nums[j+x_index+1] for j in i]
                result.append(temp)
        return list(set(result))

    def twoSum(self, nums, target):
        num_dict = {}
        index_two = []
        for idx, n in enumerate(nums):
            if target-n in num_dict:
                index_two.append([num_dict[target-n], idx])
            else:
                num_dict[n] = idx
        return index_two

# Time limit exceed
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         result = {}
#         index = 0
#         for i in range(len(nums)-2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             start = i+1
#             end = len(nums)-1
#             while(start < end):
#                 t = nums[start] + nums[end] + nums[i]
#                 if t == 0:
#                     temp = [nums[i], nums[start], nums[end]]
#                     if temp not in result.values():
#                         result[index] = temp
#                         index += 1
#                     start = start + 1
#                     end = end - 1
#                 elif t > 0:
#                     end = end - 1
#                 else:
#                     start = start + 1
#         return list(result.values())

# Accept
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        if len(nums) < 3:
            return res

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i] ,nums[l] ,nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif s < 0 :
                    l += 1
                else:
                    r -= 1
        return res 

s = Solution()
grid = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(grid))






