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

# solution 2
# no sort, time complexity is O(n)
from collections import Counter
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for str_ in strs:
            hash_id = self.getHash(str_)
            # print(hash_id)
            if hash_id not in result:
                result[hash_id] = [str_]
            else:
                result[hash_id].append(str_)
        return [result[x] for x in result]
        
        
    def getHash(self, input_str):
        hash_id = ['0' for i in range(26)]
        for h in input_str:
            hash_id[ord(h)-ord('a')] = str(int(hash_id[ord(h)-ord('a')]) + 1)
        # print(hash_id)
        return "".join(hash_id)
        
