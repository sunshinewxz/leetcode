class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        sliding_win = collections.OrderedDict()
        left = 0
        result = 0
        for i in range(len(tree)):
            sliding_win[tree[i]] = sliding_win.get(tree[i], 0) + 1
            while(len(sliding_win)>2):
                sliding_win[tree[left]] -= 1
                if sliding_win[tree[left]] == 0:
                    del sliding_win[tree[left]]
                left += 1
            result = max(result, i-left+1)
        return result

# solution 2
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        a,b = None, None
        b_num = 0
        result = 0
        cur = 0
        for c in tree:
            if c == b:
                cur += 1
                b_num += 1
            elif c == a:
                cur += 1
                b_num = 1
                a, b = b, c
            else:
                cur = b_num + 1
                b_num = 1
                a, b = b, c
            result = max(result, cur)
        return result