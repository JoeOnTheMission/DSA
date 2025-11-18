class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = [num for num in range(len(nums)+1)]
        for num in n:
            if num not in nums:
                return num