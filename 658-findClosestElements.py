import bisect
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        index = bisect.bisect_left(arr, x)
        left = index-1
        right = index
        num = 1
        result = []
        while (left >= 0 and right < len(arr) and num <= k):
            if abs(arr[left] - x) <= abs(arr[right] - x):
                result.append(arr[left])
                num += 1
                left -= 1
            else:
                result.append(arr[right])
                num += 1
                right += 1
        if len(result) < k:
            temp = arr[left+1 - (k - len(result)):left + 1] if left >= 0 else arr[right:right + k - len(result)]
            result = result + temp
        result = sorted(result)
        return result

# solution 2
def findClosestElements(self, arr, k, x):
    left = right = bisect.bisect_left(arr, x)
    while right - left < k:
        if left == 0: return arr[:k]
        if right == len(arr): return arr[-k:]
        if x - arr[left - 1] <= arr[right] - x: left -= 1
        else: right += 1
    return arr[left:right]