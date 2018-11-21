class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        index, i = 0, 0
        while(i < len(chars)):
            char = chars[i]
            length = 1
            while (i+1 < len(chars) and char == chars[i+1]):
                length += 1
                i += 1
            chars[index] = char
            if length > 1:
                digit = str(length)
                chars[index + 1: len(digit) + index + 1] = digit
                index += len(digit)
            index += 1
            i += 1
        return index