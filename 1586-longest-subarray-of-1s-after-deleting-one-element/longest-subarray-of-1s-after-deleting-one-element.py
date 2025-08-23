class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        remove = 1
        window = []

        max_length = 0
        for r in range(len(nums)):
            window.append(nums[r])
            if nums[r] == 0:
                remove -= 1
            while remove < 0:
                if nums[l] == 0:
                    remove += 1
                window.pop(0)
                l += 1
            if r - l + 1 > max_length:
                max_length = r - l
        return max_length