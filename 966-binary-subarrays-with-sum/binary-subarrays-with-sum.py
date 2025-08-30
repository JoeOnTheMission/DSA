class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        total = 0
        res = 0
        for num in nums:
            total += num
            if (total - goal) in seen:
                res += seen[total-goal]
            seen[total] += 1
        return res
