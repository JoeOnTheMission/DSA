class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        l = 0
        for r in range(len(nums)):
            d[nums[r]] = d.get(nums[r],0) + 1
            if d[nums[r]] == 1:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
        return l