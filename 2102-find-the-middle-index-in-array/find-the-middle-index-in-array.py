class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre =[0]
        total_p = 0
        suf = [0]
        total_s = 0
        j = -1
        for i in range(len(nums)-1):
            total_p += nums[i]
            pre.append(total_p)
            total_s += nums[j]
            suf.append(total_s)
            j -= 1
        suf.reverse()
        for i in range(len(pre)):
            if pre[i] == suf[i]:
                return i
        return -1