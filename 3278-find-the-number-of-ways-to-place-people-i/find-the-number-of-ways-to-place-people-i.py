class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        N = len(points)
        count = 0

        for i in range(N):
            ax, ay = points[i]
            for j in range(N):
                if i == j:
                    continue
                # a is on the lower right, j is on the upper left
                # j's x is smaller
                # j's y is larger
                bx, by = points[j]

                if not (by >= ay and bx <= ax):
                    continue

                found = False
                for k in range(N):
                    if i == k or j == k:
                        continue
                    cx, cy = points[k]
                    if bx <= cx <= ax and by >= cy >= ay:
                        found = True
                        break

                if not found:
                    count += 1

        return count
