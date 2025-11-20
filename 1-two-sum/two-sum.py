class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            needed = target - nums[i]
            if needed in nums:
                if nums.index(needed) == i:
                    i += 1 
                    continue
                else:
                    return [i,nums.index(needed)]
                    break
            i += 1
         