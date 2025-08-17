class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        if target in nums:
            target_index = nums.index(target)
            res = [ ]

            for i in range(nums.count(target)):
                res.append(target_index+i)
            return res
        else:
            return []
        