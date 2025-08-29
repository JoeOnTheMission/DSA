class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        pre = defaultdict(int)
        pre[0] = 1
        res = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            dif = total % k
            res += pre[dif]
            pre[total % k] +=1
        return res 