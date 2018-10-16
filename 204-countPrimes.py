class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        result_temp = [1 for i in range(n)]
        result_temp[0] = 0
        result_temp[1] = 0
        for i in range(2, int(n**0.5)+1):
            index = 2*i
            while(index < n):
                if result_temp[index] != 0:
                    result_temp[index] = 0
                index += i
        print(result_temp)
        return sum(result_temp)

# solution 2: faster
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        primes = [1]*n
        primes[0] = 0
        primes[1] = 0
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i] = [0]*len(primes[i*i:n:i])
        return sum(primes)

s = Solution()
print(s.countPrimes(10))
