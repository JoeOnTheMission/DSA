class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        seen = defaultdict(int)
        pairs = 0

        for num in nums:
            if k - num in seen:
                seen[k - num] -= 1
                pairs += 1

                if seen [k - num] == 0:
                    del seen[k - num]
                
            else:
                seen[num] +=1
        return pairs