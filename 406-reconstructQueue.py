# Solution 1
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sort_peo = sorted(people)
        sort_peo = sorted(sort_peo, key=lambda v:v[1])
        result = []
        while(len(sort_peo) > 0):
            if sort_peo[0][1] == 0:
                result.append(sort_peo[0])
                sort_peo.pop(0)
                continue
            num = 0
            for i in range(len(result)):
                # print(temp[0])
                if result[i][0] >= sort_peo[0][0]:
                    num += 1
                if num == sort_peo[0][1] and ((i+1 < len(result) and result[i+1][0] >= sort_peo[0][0]) or i+1 >= len(result)):
                    result = result[:i+1] + [sort_peo[0]] + result[i+1:]
                    sort_peo.pop(0)
                    break
        return result


# Solution 2: optimization
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sort_peo = sorted(people, key=lambda v:(v[0],-v[1]), reverse=True)
        result = []
        for i in range(len(sort_peo)):
            result.insert(sort_peo[i][1], sort_peo[i])
        return result
