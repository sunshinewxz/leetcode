class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded = "".join([str(len(i)) + ':' + i for i in strs])
        print(encoded)
        return encoded
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        i = 0
        result = []
        while(i < len(s)):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            result.append(s[j+1:i])
        return result
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))