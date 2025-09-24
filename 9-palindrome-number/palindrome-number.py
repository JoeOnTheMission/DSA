class Solution:
    def isPalindrome(self, x: int) -> bool:
        check = str(x)
        if check == check[::-1]:
            return True
        return False 
