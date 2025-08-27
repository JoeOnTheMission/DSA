class Solution:
    def largestNumber(self, nums: List[int]) -> str:             
        s = [str(num) for num in nums]
        for n in range(len(s)):
            for i in range(len(s)-1):
                if s[i+1]+s[i] > s[i]+s[i+1]:
                    s[i],s[i+1] = s[i+1],s[i]
        res ="".join(s)
        return str(int(res))