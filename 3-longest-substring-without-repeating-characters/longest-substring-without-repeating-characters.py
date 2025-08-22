class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        now = 0
        seen = set()
        maximum = 0

        while now < len(s):
            if s[now] in seen:
                seen.discard(s[start])
                start += 1
            else:
                seen.add(s[now])
                maximum = max(maximum, now - start + 1)
                now += 1
        return maximum