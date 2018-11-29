class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = collections.defaultdict(list)
        for i,n in enumerate(nums):
            if len(dict[n]) > 0:
                dict[n].append([i-dict[n][-1][1],i])
            else:
                dict[n] = [[i,i]]
        for key in dict:
            if len(dict[key]) < 2:
                continue
            com = [i[0] for i in dict[key]][1:]
            if min(com) <= k:
                return True
        return False