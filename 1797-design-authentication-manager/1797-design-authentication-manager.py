class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self._time = timeToLive
        self._dict = collections.OrderedDict()
    
    def _evict(self, currentTime):
        while self._dict and next(iter(self._dict.values())) <= currentTime:
            self._dict.popitem(last=False)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self._evict(currentTime)
        self._dict[tokenId] = currentTime + self._time # put new keys at the tail (the newest)

    def renew(self, tokenId: str, currentTime: int) -> None:
        self._evict(currentTime)
            
        if tokenId not in self._dict:
            return
        self._dict.move_to_end(tokenId) # the renew key must be the newest, so move to tail
        self._dict[tokenId] = currentTime + self._time

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._evict(currentTime)
        return len(self._dict)