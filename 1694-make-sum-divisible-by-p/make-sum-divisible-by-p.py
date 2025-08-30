class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) % p == 0:
            return 0       
        elif sum(nums) < p:
            return -1 
        pre =[0]
        total = 0
        remainder = sum(nums) % p
        for num in nums:#construct prefix sum
            total += num
            pre.append(total)

        seen = defaultdict(list)
        res = len(nums)
        for i in range(len(pre)):
            if (pre[i] - remainder ) % p in seen:
                y = max(seen[(pre[i]-remainder) % p])
                res = min(res,i-y)
            seen[pre[i] % p].append(i)

        return res if res!= len(nums) else -1