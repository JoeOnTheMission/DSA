class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        seen = defaultdict(int)
        res = 0
        for num in nums:
            seen[num] += 1
        i = 0
        for num in seen:
            res += seen[num] * i
            i += 1
        return res