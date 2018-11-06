# time limited error
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def backtrack(temp, target, subnums):
            if len(temp) == 3 and target > 0:
                result.append(temp[:])
            if len(temp) > 3:
                return
            for i in range(len(subnums)):
                temp.append(subnums[i])
                backtrack(temp, target-subnums[i], subnums[i+1:])
                temp.pop()
        nums = sorted(nums, reverse = True)
        result = []
        backtrack([], target, nums)
        return len(result)


# solution 2: O(n^2)
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        nums = sorted(nums)
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while(j < k):
                if nums[i] + nums[j] + nums[k] < target:
                    result += k - j
                    j += 1
                else:
                    k -= 1
        return result