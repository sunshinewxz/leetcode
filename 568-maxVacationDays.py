class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        graph = {}
        for i in range(len(flights)):
            graph[i] = [i]
            for j in range(len(flights[0])):
                if flights[i][j] == 1:
                    graph[i].append(j)
        dp = [[0] * len(days[0]) for i in range(len(flights))]
        for c in range(len(flights)):
            dp[c][len(days[0])-1] = days[c][len(days[0])-1]
        for w in range(len(days[0])-2, -1, -1):
            for c in range(len(flights)):
                dp[c][w] = max(days[c][w] + dp[n][w+1] for n in graph[c])
        return max([dp[c][0] for c in graph[0]])