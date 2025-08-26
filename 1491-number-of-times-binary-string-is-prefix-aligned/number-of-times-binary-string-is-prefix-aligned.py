class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        string = [0]*(len(flips)+1)
        r = 1
        res = 0
        for i in range(len(flips)):
            string[flips[i]] = 1
            while r < len(string) and string[r] == 1:
                r += 1
            if i + 1 == r - 1:
                res += 1
        return res 