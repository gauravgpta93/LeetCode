import random
import string


class Codec:
    LETTERS = string.ascii_letters + "0123456789"
    BASE_ADDRESS = 'http://tinyurl.com/'

    def __init__(self):
        self._encoded = dict()
        self._decoded = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self._decoded:
            short_code = "".join(random.choice(Codec.LETTERS) for i in range(6))
            if short_code not in self._encoded:
                self._encoded[short_code] = longUrl
                self._decoded[longUrl] = short_code
        return "".join([Codec.BASE_ADDRESS, self._decoded[longUrl]])

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self._encoded.get(shortUrl[-6:])

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
