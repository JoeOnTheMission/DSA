class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        can_start = 0
        for r in range(len(nums)):

            if nums[r] % 2 != 0:#odd
                k -= 1
                can_start = 0

            while k == 0:
                if nums[l] % 2 != 0:#odd
                    k += 1
                l += 1

                can_start += 1
            res += can_start
        return res