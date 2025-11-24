class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        needed = set(range(left,right+1))
        contained = set()
        for start,end in ranges:
            contained.update(range(start,end + 1))
        return needed.issubset(contained)