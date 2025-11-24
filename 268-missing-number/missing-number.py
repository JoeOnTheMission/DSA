class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        solution = len(nums)
        for i,num in enumerate(nums):
            solution ^= i^num
        return solution 