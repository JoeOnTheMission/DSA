class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind,i in enumerate(nums):
            x = target - i
            if x in nums:
                if ind == nums.index(x):
                    continue
                return [ind , nums.index(x)]