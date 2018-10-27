class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, end):
            if start == end and nums not in result:
                result.append(nums[:])
            else:
                for i in range(start, end):
                    if i != start and nums[i] == nums[start]:
                        continue
                    nums[i], nums[start] = nums[start], nums[i]
                    backtrack(start+1, end)
                    nums[i], nums[start] = nums[start], nums[i]
                    
        nums = sorted(nums)
        result = []
        backtrack(0, len(nums))
        return result

# solution 2
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(temp, size):
            if len(temp) == size:
                result.append(temp[:])
            else:
                for i in range(size):
                    if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                        continue
                    else:
                        temp.append(nums[i])
                        visited[i] = True
                        backtrack(temp, size)
                        temp.pop()
                        visited[i] = False
                    
        nums = sorted(nums)
        result = []
        visited = [False] * len(nums)
        backtrack([], len(nums))
        return result