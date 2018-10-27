class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i+1 for i in range(n)]
        fact = [1] * n
        for i in range(1, n):
            fact[i] = i * fact[i-1]
        k -= 1
        result = []
        for i in range(n-1, -1, -1):
            id = k // fact[i]
            k = k % fact[i]
            result.append(str(nums[id]))
            nums.pop(id)
        return "".join(result)