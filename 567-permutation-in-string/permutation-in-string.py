class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        if len(s1) >len(s2):
            return False

        l = 0
        window = defaultdict(int)
        target = defaultdict(int)


        for char in s1:
            target[char] += 1
            window[s2[l]] += 1
            l += 1
        
        if window == target:
           return True
   
        for l in range(len(s2)-len(s1)):
            r = l + len(s1)
            window[s2[l]] -= 1
            window[s2[r]] += 1
            if window[s2[l]] == 0:
                del window[s2[l]]

            if window == target:
                return True
        return False