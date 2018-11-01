class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        moves = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]}
        result = 0
        used = set()
        ori = "".join([str(a) for row in board for a in row])
        temp = [[ori, ori.index('0')]]
        while(len(temp) > 0):
            new = []
            for t in temp:
                if t[0] == '123450':
                    return result
                used.add(t[0])
                arr = list(t[0])
                for move in moves[t[1]]:
                    new_arr = arr[:]
                    new_arr[move], new_arr[t[1]] = new_arr[t[1]], new_arr[move]
                    new_str = "".join(new_arr)
                    if new_str not in used:
                        new.append([new_str, move])
            result += 1
            temp = new
        return -1

        