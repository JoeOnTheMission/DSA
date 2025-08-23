class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        remove = 1

        max_length = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                remove -= 1
            while remove < 0:
                if nums[l] == 0:
                    remove += 1
                l += 1
            if r - l + 1 > max_length:
                max_length = r - l
        return max_length