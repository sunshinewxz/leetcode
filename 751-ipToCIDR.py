class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        ip_int = int.from_bytes(bytes(map(int, ip.split('.'))), 'big')
        result = []
        while(True):
            low_digit = ip_int & (-ip_int)
            if low_digit > n:
                break
            result.append(ip+'/' + str(32-low_digit.bit_length()+1))
            ip_int += low_digit
            ip = ".".join(map(str, ip_int.to_bytes(4, 'big')))
            n -= low_digit
        
        while(n > 0):
            i = n.bit_length()
            result.append(ip+'/'+str(32-i+1))
            low_digit = 1 << i-1
            ip_int += low_digit
            ip = ".".join(map(str, ip_int.to_bytes(4, 'big')))
            n -= low_digit
        return result
            