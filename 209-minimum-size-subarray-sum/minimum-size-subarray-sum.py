class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        current_sum = 0
        if current_sum >= target:
            return 1
        res = len(nums)
        # length = r - l + 1
        for r in range(len(nums)):
            current_sum += nums[r]

            while current_sum >= target:
                res = min(res, r - l + 1)
                current_sum -= nums[l]
                l += 1
        if sum(nums) < target:
            return 0
        return res