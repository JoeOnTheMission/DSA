class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        from collections import defaultdict

                
        wall_set = {(wx, wy) for wx, wy in walls}
        guard_set = {(gx, gy) for gx, gy in guards}

        vision = defaultdict(set)

        for guard in guards:
            x = guard[0]
            y = guard[1]
            while x > 0:# UP
                x -= 1
                if (x, y) in wall_set or (x, y) in guard_set:
                    break
                vision[x].add(y)
            x = guard[0]
            y = guard[1]
            while x < m -1: # DOWN
                x += 1
                if (x, y) in wall_set or (x, y) in guard_set:
                    break
                vision[x].add(y)
            x = guard[0]
            y = guard[1]
            while y < n - 1:# RIGHT
                y += 1
                if (x, y) in wall_set or (x, y) in guard_set:
                    break
                vision[x].add(y)
            x = guard[0]
            y = guard[1]
            while y > 0:  # LEFT
                y -= 1
                if (x, y) in wall_set or (x, y) in guard_set:
                    break
                vision[x].add(y)
        blocked = set(wall_set) | set(guard_set)
        for x in vision:
            for y in vision[x]:
                blocked.add((x, y))

        return m * n - len(blocked)
  