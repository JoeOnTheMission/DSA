class Solution:
    def smallestNumber(self, num: int) -> int:
        digits = [d for d in str(num) if d != "-"]
        i = 1
        if str(num)[0] == "-":#-ve
            digits.sort(reverse=True)
            while digits[0] =="0" and i < len(str(num)):
                digits[0],digits[i] = digits[i], digits[0]
                i += 1
            return int("".join(digits)) * -1
        else:#+ve
            digits.sort()
            while digits[0] =="0" and i < len(str(num)):
                digits[0],digits[i] = digits[i], digits[0]
                i += 1
            return int("".join(digits))