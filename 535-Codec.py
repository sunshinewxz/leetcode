class Codec:
    def __init__(self):
        self.dict = {}
        self.key = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.key += 1
        shorturl = 'tinyurl' + str(self.key)
        self.dict[shorturl] = longUrl
        return shorturl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.dict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))