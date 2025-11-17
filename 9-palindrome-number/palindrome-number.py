class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        org = x
        rev = 0
        while org > 0:
            a = org % 10
            rev = rev*10 + a
            org = org // 10
        return x == rev