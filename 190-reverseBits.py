class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        str_n = bin(n)[2:]
        add = 32-len(str_n)
        str_n = '0'*add + str_n
        str_n = str_n[::-1]
        return int(str_n, 2)