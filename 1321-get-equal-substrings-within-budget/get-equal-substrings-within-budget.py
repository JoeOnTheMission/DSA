class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        l = 0
        window_sum = 0
        max_length = 0

        for r in range(len(t)):
            window_sum += abs(ord(s[r]) - ord(t[r]))
            while window_sum > maxCost:
                window_sum -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            if r - l + 1 > max_length:
                max_length = r - l + 1
        return max_length