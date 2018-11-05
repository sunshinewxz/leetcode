class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + '->' + str(upper)]
        if len(nums) == 1:
            if nums[0]-1 > lower:
                result.append(str(lower) + '->' + str(nums[0]-1))
            elif nums[0]-1 == lower:
                result.append(str(lower))
            if nums[0]+1 == upper:
                result.append(str(upper))
            elif nums[0]+1 < upper:
                result.append(str(nums[0]+1) + '->' + str(upper))
            return result
        low = high = lower
        stack = []
        for i in range(len(nums)):
            if len(stack) == 0:
                stack.append(nums[i])
                continue
            cur = stack.pop()
            if i == 1 and cur-1 > lower:
                result.append(str(lower) + '->' + str(cur-1))
            elif i == 1 and cur-1 == lower:
                result.append(str(lower))
            if cur+2 == nums[i]:
                result.append(str(cur+1))
            elif cur+2 < nums[i]:
                result.append(str(cur+1) + '->' + str(nums[i]-1))
            stack.append(nums[i])
        if len(stack) > 0:
            cur = stack.pop()
            if cur + 1 == upper:
                result.append(str(upper))
            elif cur + 1 < upper:
                result.append(str(cur+1) + '->' + str(upper))
        return result
                
# solution 2: more concise
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        nums.append(upper+1)
        pre = lower - 1
        for n in nums:
            if pre+2 == n:
                result.append(str(pre+1))
            elif pre+2 < n:
                result.append(str(pre+1) + '->' + str(n-1))
            pre = n
        return result
            