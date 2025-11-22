class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        solution = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left += 1
                if left == right:
                    right += 1
            else:
                solution = max(solution,profit)
                right += 1
        return solution 