class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            length = 0
            point = set()
            temp = i
            positive = nums[i] > 0
            while(length <= len(nums)):
                if nums[temp] > 0 and positive:
                    nums[temp] = nums[temp] % len(nums)
                    if temp + nums[temp] > len(nums) - 1:
                        next_index = temp + nums[temp] - len(nums)
                    else:
                        next_index = temp + nums[temp]

                elif nums[temp] < 0 and not positive:
                    nums[temp] = -((-nums[temp]) % len(nums))
                    if temp + nums[temp] < 0:
                        next_index = len(nums) + temp + nums[temp]
                    else:
                        next_index = temp + nums[temp]

                if next_index == i and len(point) >= 2:
                        return True
                length += 1
                point.add(temp)
                temp = next_index
        return False

s = Solution()
print(s.circularArrayLoop([3,1,2]))


