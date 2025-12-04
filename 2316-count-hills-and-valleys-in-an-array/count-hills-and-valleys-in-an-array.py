class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        unique_nums = []
        last_seen = None
        for num in nums:
            if num == last_seen:
                continue
            unique_nums.append(num)
            last_seen = num
        print(unique_nums)
        #i , j , k
        res = 0
        for j in range(1 , len(unique_nums) - 1):
            if unique_nums[j-1] < unique_nums[j] > unique_nums[j+1] or unique_nums[j-1] > unique_nums[j] < unique_nums[j+1]:
                res += 1
        return res