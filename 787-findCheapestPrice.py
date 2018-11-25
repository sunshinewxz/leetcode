import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        flight_connect = collections.defaultdict(dict)
        for a,b,p in flights:
            flight_connect[a][b] = p
        # heap: [price, place, stop_num]
        heap = [[0, src, K+1]]
        while(len(heap) > 0):
            price, place, stop_num = heapq.heappop(heap)
            if place == dst:
                return price
            if stop_num > 0:
                for next_place in flight_connect[place]:
                    heapq.heappush(heap, [price + flight_connect[place][next_place], next_place, stop_num-1])
        return -1