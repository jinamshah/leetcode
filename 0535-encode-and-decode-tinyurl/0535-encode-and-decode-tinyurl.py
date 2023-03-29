import uuid
class Codec:
    def __init__(self):
        self.hashset=set()
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encodedUrls = [x[0] for x in self.hashset]
        if longUrl not in encodedUrls:
            self.hashset.add((longUrl,str(uuid.uuid4())))
        return [x[1] for x in self.hashset if x[0] == longUrl][0]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        print(self.hashset)
        print("asdas: ",shortUrl)
        decodedUrls = [x[0] for x in self.hashset if x[1] == shortUrl]
        return decodedUrls[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))