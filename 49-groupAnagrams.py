class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        base = []
        for str_single in strs:
            str_single = str(sorted(list(str_single)))
            if str_single not in base:
                base.append(str_single)

        result = [[] for i in range(len(base))]
        for str_single in strs:
            index = base.index(str(sorted(list(str_single))))
            result[index].append(str_single)
        return result


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))
