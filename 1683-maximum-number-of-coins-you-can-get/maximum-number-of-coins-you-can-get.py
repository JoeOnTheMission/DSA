class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        last = piles[len(piles) - 1]
        mine = piles[len(piles) - 2]
        first = piles[0]
        res = 0
        for i in range(len(piles)//3):
            last = piles[len(piles) - 1 ]
            mine = piles[len(piles) - 2 ]
            first = piles[0]

            res += mine

            piles.pop(len(piles) - 1 )
            piles.pop(len(piles) - 1 )
            piles.pop(0)
        return res