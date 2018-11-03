import collections
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        node_graph = collections.defaultdict(dict)
        for t in times:
            node_graph[t[0]][t[1]] = t[2]
        time = [None] * (N+1)
        cur_layer = [K]
        time[0] = 0
        next_layer = set()
        time[K] = 0
        while(len(cur_layer) > 0):
            while(len(cur_layer) > 0):
                node = cur_layer.pop()
                for next in node_graph[node]:
                    if time[next] is None or time[next] > time[node] + node_graph[node][next]:
                        time[next] = time[node] + node_graph[node][next]
                        next_layer.add(next)
            cur_layer = list(next_layer)
            next_layer = set()
        max_t = -1
        for i in range(N+1):
            if time[i] == None:
                return -1
            max_t = max(max_t, time[i])
        return max_t
                        
                    