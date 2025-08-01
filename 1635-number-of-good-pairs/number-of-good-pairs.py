class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        number_of_good_pairs = 0
        unique_of_pair = []

        for num in nums:
            if num not in unique_of_pair:
                if nums.count(num) > 1:
                    unique_of_pair.append(num)

        for number in unique_of_pair:
            count = nums.count(number)
            number_of_good_pairs += count * (count - 1) // 2

        return number_of_good_pairs