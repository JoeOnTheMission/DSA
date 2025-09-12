class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for a in range(len(nums)-2):
            left = a + 1
            right = len(nums) - 1
            while left < right:
                total = nums[a]+nums[left]+nums[right]
                if abs(total - target) < abs(res - target):
                    res = total
                if total == target:
                    return total 
                elif total < target:
                    left += 1
                else:
                    right -=1
        return res