class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checker = set(nums)
        if len(nums) == len(checker):
            return False
        else:
            return True 