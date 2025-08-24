class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        can_start = 0
        odd = 0
        for r in range(len(nums)):
            if nums[r] % 2: #num is odd
                odd += 1
            while odd > k:
                if nums[l] % 2:
                    odd -= 1
                l += 1
                can_start = l
            if odd == k:
                while not nums[can_start] % 2: #every even point from here makes a valid subarray until r
                    can_start += 1
                res += (can_start - l) + 1
        return res