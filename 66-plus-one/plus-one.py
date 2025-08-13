class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = 10 ** len(digits)//10
        res = 0
        final = []
        for i in digits:
            res = res + (i * x)
            x = x//10
        res = res + 1
        while res:
            final.append(res % 10)
            res = res //10
        return final[::-1]