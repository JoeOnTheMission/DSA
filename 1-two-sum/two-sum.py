class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index,num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [index,seen[needed]]
            else:
                seen[num] = index
        