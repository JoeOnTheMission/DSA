class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = set()
        for left in range(len(nums)-(len(nums)//3)):
            right = left + len(nums)//3
            if nums[left] == nums[right]:
                res.add(nums[left])
        return list(res)