class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        res = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:#child take
                res += 1
                child += 1
                cookie += 1
            else:#child not take but cookie change
                cookie += 1
        return res