class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # left_multi = [1 for i in range(len(nums))]
        # right_multi = [1 for i in range(len(nums))]

        # result = []
        # for i in range(len(nums)-1):
        #     left_multi[i+1] = left_multi[i] * nums[i]
        #     right_multi[len(nums)-i-2] = right_multi[len(nums)-i-1] * nums[len(num)-i-1]

        # for i in range(len(nums)):
        #     result.append(left_multi[i] * right_multi[i])
        # return result

        # follow up: constant space complexity
        result = [1 for i in range(len(nums))]
        right_product = 1

        for i in range(len(nums)-1):
            result[i+1] = result[i] * nums[i]

        for i in range(len(nums)-2,-1,-1):
            right_product *= nums[i+1]
            result[i] = result[i] * right_product

        return result
s = Solution()
print(s.productExceptSelf([1,2,3,4]))
