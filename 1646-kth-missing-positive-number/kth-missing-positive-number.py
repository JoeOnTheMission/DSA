class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        count_of_missing_numbers = 0

        for num in arr:
            missing = num - left - 1
            count_of_missing_numbers += missing
            if count_of_missing_numbers >= k:
                return num - 1 - (count_of_missing_numbers - k)
            left = num
        return arr[-1] + (k - count_of_missing_numbers)