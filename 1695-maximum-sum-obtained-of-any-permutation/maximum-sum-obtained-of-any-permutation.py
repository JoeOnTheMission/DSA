class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:                
        req = [0]*(len(nums) + 1)
        for start,end in requests:#construct req
            req[start] += 1
            req[end + 1] -= 1

        
        total = 0
        for i in range(len(req)):#prefix sum req
            total += req[i]
            req[i] = total

        req = req[:-1]  
        req.sort(reverse=True)
        nums.sort(reverse=True)
        MOD = 10**9 + 7
        res = 0
        for i in range(len(nums)):
            res = (res + nums[i] * req[i]) % MOD
        return res