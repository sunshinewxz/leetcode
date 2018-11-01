from heapq import *
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tic_dict = {}
        for t in tickets:
            if t[0] in tic_dict:
                heappush(tic_dict[t[0]], t[1])
            else:
                tic_dict[t[0]] = [t[1]]
        print(tic_dict)
        route = []
        start = 'JFK'
        def dfs(at):
            while(at in tic_dict and len(tic_dict[at]) > 0):
                to = heappop(tic_dict[at])
                dfs(to)
            route.append(at)
            
        dfs(start)
        return route[::-1]