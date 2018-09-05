def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    nums.sort(reverse=False)
    sum = nums[0] + nums[1] + nums[2]
    dis = abs(sum - target)
    for i in range(len(nums)):
        x = nums[i]
        start = i+1
        end = len(nums)-1
        while(start<end):
            temp = x + nums[start] + nums[end]
            if abs(temp-target)<dis:
                dis = abs(temp - target)
                sum = temp
            if temp<target:
                start += 1
            elif temp>target:
                end -= 1
            else:
                return temp
    return sum




nums = [-3,-2,-5,3,-4]
target = -1
sum = threeSumClosest(nums,target)
print(sum)
