class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(2):
            res.extend(nums)
        return res