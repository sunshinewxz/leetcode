class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        nums = collections.Counter(s)
        mid = [char for char, num in nums.iteritems() if num%2 == 1]
        if len(mid) > 1:
            return []
        mid = '' if len(mid) == 0 else mid[0]
        half = "".join([char*(num/2) for char, num in nums.iteritems()])
        half = [h for h in half]
        
        def backtrack(temp, end):
            if len(temp) == end:
                cur = "".join(temp)
                result.append(cur + mid + cur[::-1])
            else:
                for i in range(end):
                    if visited[i] or (i > 0 and half[i]==half[i-1] and not visited[i-1]):
                        continue
                    visited[i] = True
                    temp.append(half[i])
                    backtrack(temp, end)
                    temp.pop()
                    visited[i] = False
        
        result = []
        visited = [False] * len(half)
        backtrack([], len(half))
        return result