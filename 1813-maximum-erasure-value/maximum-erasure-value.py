class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        window = set()
        window_sum = 0
        res = 0
        for r in range(len(nums)):

            while nums[r] in window:
                window.remove(nums[l])
                window_sum -= nums[l]
                l += 1
            window.add(nums[r])
            window_sum += nums[r]
            res = max(res,window_sum)
        return res