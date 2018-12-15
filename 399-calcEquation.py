class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        digits = collections.defaultdict(dict)
        for (a,b),v in zip(equations, values):
            digits[a][a] = digits[b][b] = 1.0
            digits[a][b] = v
            digits[b][a] = 1.0/v
        for d in digits:
            for i in digits[d]:
                for j in digits[d]:
                    digits[i][j] = digits[i][d] * digits[d][j]
        return [digits[a].get(b,-1.0) for a,b in queries]