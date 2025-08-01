class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        is_divisible_by_3 = num % 3 == 0
        if not is_divisible_by_3:
            return []
        x = int(num / 3)
        array = [x - 1, x, x + 1]
        return array
