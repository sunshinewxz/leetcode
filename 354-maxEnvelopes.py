class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes = sorted(envelopes, key=lambda d:(d[0],-d[1]))
        height = []
        for envelop in envelopes:
            w,h = envelop
            index = bisect.bisect_left(height, h)
            if index == len(height):
                height.append(h)
            else:
                height[index] = h
        return len(height)
                