class Solution:
    def balancedString(self, s: str) -> int:
        from collections import defaultdict
        
        n = len(s)
        balanced_count = n//4
        to_be_replaced = defaultdict(int)
        for letter in "QWER":
            to_be_replaced[letter] = max(0,s.count(letter) - balanced_count)
       
        if sum(to_be_replaced.values()) == 0:#already balanced
           return 0
        res = n #worst case we replace every thing
        l = 0
        for r in range(n):
            to_be_replaced[s[r]] -= 1
            while l < n and all(to_be_replaced[letter] <= 0 for letter in "QWER"):#every thing outside window count is less than balanced count AKA valid window
                res = min(res, r - l + 1)
                to_be_replaced[s[l]] += 1
                l += 1
        return res 