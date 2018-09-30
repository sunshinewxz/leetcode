import numpy as np
class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r in range(N):
                for c in range(N):
                    for dr, dc in zip((2, 2, -2, -2, 1, 1, -1, -1), (1, -1, 1, -1, 2, -2, 2, -2)):
                        if 0 <= r+dr < N and 0 <= c+dc < N:
                            dp2[r+dr][c+dc] += (dp[r][c]/8.0)
            dp = dp2
        return np.sum(dp)

# solution 2
class Solution:
    def knightProbability(self, N, K, r, c):        
        pr = [[[0] * K for j in range(N)] for i in range(N)]
        def probab(N, K, r, c):
            if K == 0:
                return 1
            elif pr[r][c][K - 1] > 0:
                return pr[r][c][K - 1]
            p = 0
            for move in [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]]:
                rr, cc = r + move[0], c + move[1]
                if -1 < rr < N and -1 < cc < N:
                    p += 0.125 * probab(N, K - 1, rr, cc)
            pr[r][c][K - 1], pr[c][r][K - 1] = p, p
            pr[r][N - 1 - c][K - 1], pr[c][N - 1 - r][K - 1] = p, p
            pr[N - 1 - r][c][K - 1], pr[N - 1 - c][r][K - 1] = p, p
            pr[N - r - 1][N - c - 1][K - 1], pr[N - c - 1][N - r - 1][K - 1] = p, p
            return p
        p = probab(N, K, r, c)
        return p


s = Solution()
N, K, r, c = 3, 2, 0, 0
result = s.knightProbability(N, K, r, c)
print(result)


