class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(temp, start, end, target):
            if target == 0:
                result.append(temp[:])
            elif target > 0:
                for i in range(start, end):
                    temp.append(candidates[i])
                    backtrack(temp, i, end, target-candidates[i])
                    temp.pop()
        
        result = []
        candidates = sorted(candidates, reverse=True)
        backtrack([], 0, len(candidates), target)
        return result