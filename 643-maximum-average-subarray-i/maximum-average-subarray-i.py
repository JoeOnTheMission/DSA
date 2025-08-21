class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = l + k
        window_sum =sum(nums[:r])
        max_sum = window_sum
        while l < len(nums) - k:
            window_sum = window_sum - nums[l] + nums[r]
            if window_sum > max_sum:
                max_sum = window_sum
            l += 1
            r = l + k
        return max_sum / k
    