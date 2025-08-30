class Solution:
    def maxScore(self, s: str) -> int:
        total = sum([int(num) for num in s])
        right = total
        left = 0
        res = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                left += 1
            else:
                right -= 1
            res = max(left+right,res)
        return res 