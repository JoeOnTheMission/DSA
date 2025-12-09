class RecentCounter:

    def __init__(self):
        self.queue = []
        self.headIndex = 0
    def ping(self, t: int) -> int:
        self.queue.append(t)
        while (t - self.queue[self.headIndex]) > 3000:
            self.headIndex += 1
        return len(self.queue) - self.headIndex
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)