class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def number_to_ternary(n):
            ternary_digits = []
            while n > 0:
                remainder = n % 3
                ternary_digits.append(remainder)
                n //= 3
            return ternary_digits
        ternary_version = number_to_ternary(n)
        two_present = ternary_version.count(2) > 0
        if two_present:
            return False
        else:
            return True 