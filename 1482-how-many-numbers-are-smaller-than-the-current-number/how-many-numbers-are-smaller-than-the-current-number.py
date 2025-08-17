class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        res = []
        for num in nums:
            res.append(s.index(num))
        return res