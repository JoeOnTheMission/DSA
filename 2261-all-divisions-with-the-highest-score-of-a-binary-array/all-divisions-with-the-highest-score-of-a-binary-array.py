class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        i = 0
        total_ones = sum(nums)
        max_score = total_ones
        left_zeros = 0
        out_put = [0]
        for i in range(len(nums)):
            if nums[i] == 0:
                left_zeros += 1
            else:
                total_ones -= 1
            current_score = left_zeros + total_ones
            if current_score > max_score:
                max_score = current_score
                out_put = [i + 1] 
            elif current_score == max_score:
                out_put.append(i + 1)
        return out_put