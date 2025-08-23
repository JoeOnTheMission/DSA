class Solution:
    def maxVowels(self, s: str, k: int) -> int:      
        l = 0
        r = k - 1
        target = { 'a', 'e', 'i', 'o','u'}
        count = 0
        max_count = 0
        for i in range(k):
            if s[i] in target:
                count += 1
                max_count = max(max_count,count)
        if count == k:
            return count

        for l in range(len(s)-k):
            r = l + k

            if s[r] in target:
                count += 1
            if s[l] in target:
                count -= 1
            max_count = max(max_count,count)
        return max_count  