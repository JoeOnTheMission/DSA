class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        pos = []
        for p,f,t in trips:
            pos.append([f, p])
            pos.append([t, -p])
        pos.sort()
        total = 0
        for i in range(len(pos)):
            total += pos[i][1]
            if total > capacity:
                return False
        return True 