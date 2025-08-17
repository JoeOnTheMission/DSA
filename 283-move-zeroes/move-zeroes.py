class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker = 0
        place_holder = 0
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] == 0:
                place_holder = i
                for j in range(i+1 , len(nums)):
                    if nums[j] != 0:
                        seeker = j
                        nums[i],nums[j] = nums[j],nums[i]
                        break
        return nums