class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l = 0
        seen = {}
        res = float('inf')
        unique = True
        for r in range(len(cards)):
            seen[cards[r]] = seen.get(cards[r],0) + 1
            while seen[cards[r]] >= 2:
                unique = False
                if seen[cards[r]] == 2:
                    res = min(res,r - l + 1)
                seen[cards[l]] = seen.get(cards[l], 0) - 1
                l += 1
                if seen[cards[l]] == 0:
                    del seen[cards[l]]
        if unique:
            return -1
        else:
            return res