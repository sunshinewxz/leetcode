import sys

# n eggs; k floors
def eggDrop(n, k):
	max_size = sys.maxsize()
	dp = [[max_size] * (k+1) for i in range(n+1)]
	for i in range(1, n+1):
		dp[i][0] = 0
		dp[i][1] = 1

	for j in range(1, k+1):
		dp[1][j] = j

	for i in range(2, n+1):
		for j in range(2, k+1):
			for x in range(1, j+1):
				res = 1 + max(dp[i-1][x-1], dp[i][j-x])
				dp[i][j] = min(res, dp[i][j])
	return dp[n][k]