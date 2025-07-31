class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        x = n
        for i in range(1,150):
            x = n * i
            if x % 2 == 0:
                break
        return x