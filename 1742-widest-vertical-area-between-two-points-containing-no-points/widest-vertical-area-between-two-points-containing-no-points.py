class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = [ x[0] for x in points ]
        l.sort()
        max_length = 0
        for i in range(len(l) - 1 ):
            length = l[i+1] - l[i]
            if length > max_length:
                max_length = length
        return max_length