import uuid
class Codec:
    def __init__(self):
        self.hashset={}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # encodedUrls = [x[0] for x in self.hashset]
        if longUrl not in self.hashset.values():
            encoded = uuid.uuid4()
            self.hashset[encoded] = longUrl
        return encoded

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hashset[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))