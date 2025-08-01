class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        state = True
        if n <= 0 :
            return False
        x = math.log(n,3)
        check = 3 ** round(x)
        if check != n:
            state = False
        return state 