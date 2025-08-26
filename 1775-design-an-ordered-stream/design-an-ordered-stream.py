class OrderedStream:
    def __init__(self, n: int):
        self.strings = [None] *(n + 1)
        self.i = 1
    def insert(self, idkey: int, value: str) -> List[str]:
        self.strings[idkey] = value
        res = []
        while  self.i < len(self.strings) and self.strings[self.i] is not None:
            res.append(self.strings[self.i])
            self.i += 1
        return res
        
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)