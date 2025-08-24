class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        window_size = len(cardPoints) - k

        window_sum = sum(cardPoints[:window_size])
        score = total - window_sum

        for l in range(1, len(cardPoints) - window_size + 1):
            r = l + window_size - 1
            window_sum += cardPoints[r]
            window_sum -= cardPoints[l - 1]
            score = max(score, total - window_sum)
        return score 
            