class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p: int, t: int) -> float:
            return (t - p) / (t * (t + 1))

        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)  

        for _ in range(extraStudents):
            neg_g, p, t = heapq.heappop(heap) 
            p, t = p + 1, t + 1                 
            heapq.heappush(heap, (-gain(p, t), p, t)) 

        total_ratio = 0.0
        while heap:
            _, p, t = heapq.heappop(heap)
            total_ratio += p / t

        return total_ratio / len(classes)
