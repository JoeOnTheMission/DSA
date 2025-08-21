class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            start = i
            seen = {}
            still_valid = True
            length = 0 
            if nums[i] > 0:
                positive = True
            else:
                positive = False
            while still_valid:
                #print(i,nums[i])
                if i in seen:
                    break
                else:
                    seen[i] = 0
                i = (i + nums[i]) % len(nums)  # next index
                if positive and nums[i] < 0:#change in sign
                    still_valid = False
                    break
                if not positive and nums[i] > 0:#change in sign
                    still_valid = False
                    break
                length += 1


            if start == i and still_valid and length > 1:
                return True
                #print("valid found and return True",start,i)
        return False