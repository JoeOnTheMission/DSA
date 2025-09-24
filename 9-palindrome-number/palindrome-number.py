class Solution:
    def isPalindrome(self, x: int) -> bool:
        check = str(x)
        if x >= 0 and check == check[::-1]:
            return True
        return False 
