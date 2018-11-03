import bisect
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        li = list(str(n))
        temp = sorted(li, reverse = True)
        if temp == li:
            return -1
        for i in range(len(li)-1, -1, -1):
            if any(num > li[i] for num in li[i+1:]):
                new_li = sorted(li[i+1:])
                index = bisect.bisect_right(new_li, li[i])
                li[i], new_li[index] = new_li[index], li[i]
                li = li[:i+1] + new_li
                result = int("".join(li))
                return result if result < (1<<31-1) else -1
        