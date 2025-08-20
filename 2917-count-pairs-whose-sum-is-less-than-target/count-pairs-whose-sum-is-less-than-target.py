class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()           # Sort the array first
        left, right = 0, len(nums) - 1
        res = 0
        
        while left < right:
            if nums[left] + nums[right] < target:
                # All pairs (left, left+1 ... right) are valid
                res += right - left
                left += 1
            else:
                # Sum too big, try smaller sum
                right -= 1
        
        return res