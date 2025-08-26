class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.t = timeToLive
        self.map = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.map[tokenId] = currentTime + self.t     

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.map:
            if self.map[tokenId] > currentTime :
                self.map[tokenId] = currentTime + self.t  

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        for i in self.map.values():
            if i > currentTime:
                res += 1
        return res
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)