class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = c
        while l <= r:
            if (r**2)  > c:
                r = r//2
            elif(r**2)  <= c:
                r = r*2
                break
        while l <= r:
            if (r**2) + (l**2) > c:
                r -= 1
            elif(r**2) + (l**2) < c:
                l += 1
            else:
                return True
        return False 