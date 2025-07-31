class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
             return False
        
        else:
            rev = 0
            orig = x
            while x > 0:
                digit = x % 10
                rev = rev * 10 + digit 
                x //= 10
        return orig == rev