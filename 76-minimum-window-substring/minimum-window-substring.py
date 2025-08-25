class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        target = Counter(t)
        count_of_s = Counter(s)
        for letter in target:
            if target[letter] > count_of_s [letter]:
                return ""
        res = [0,len(s)-1]
        window = Counter()
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            while l < len(s) and all(window[letter] >= target[letter]  for letter in target ):#catch all valid window
                #updating res
                if res[1] - res[0] + 1 > r - l + 1:
                    res[0] = l
                    res[1] = r
                #shrinking
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
        return s[res[0]:res[1]+1]