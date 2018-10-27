class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def backtrack(start, end, temp):
            if start == end:
                result.append(temp[:])
            else:
                for i in range(start, end):
                    cur = s[start:i+1]
                    if cur == cur[::-1]:
                        temp.append(cur)
                        backtrack(i+1, end, temp)
                        temp.pop()
        result = []
        backtrack(0, len(s), [])
        return result