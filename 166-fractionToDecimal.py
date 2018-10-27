class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = []
        sign = '' if ((numerator < 0) == (denominator < 0)) or (numerator == 0) else '-'
        res.append(sign)
        numerator, denominator = abs(numerator), abs(denominator)
        mod = []
        res.append(str(numerator // denominator))
        mod.append(numerator % denominator)
        if mod[0] == 0:
            return "".join(res)
        else:
            res.append('.')
        new_mod = (mod[0]*10) % denominator
        res.append(str((mod[0]*10) // denominator))
        while (new_mod not in mod):
            if new_mod == 0:
                return "".join(res)
            mod.append(new_mod)
            res.append(str((new_mod*10)//denominator))
            new_mod = (new_mod*10) % denominator
        s = mod.index(new_mod)+3
        res = res[:s] + ['('] + res[s:len(res)] + [')']
        return "".join(res)
                