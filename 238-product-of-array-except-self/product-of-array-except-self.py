class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        suffix = [1]
        prefix = [1]
        last_s = 1
        last_p = 1
        j = -1
        for i in range(len(nums)-1):
            last_s *= nums[i]
            suffix.append(last_s)
            last_p *= nums[j]
            prefix.append(last_p)
            j -= 1
        prefix.reverse()
        res = []
        for a,b in zip(prefix,suffix):
            res.append(a*b)
        return res