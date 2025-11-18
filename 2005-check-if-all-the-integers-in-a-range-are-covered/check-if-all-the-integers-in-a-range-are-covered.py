class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        needed = [ i for i in range(left,right+1)]

        contained = []
        for pair in ranges:
            a = pair[0]
            b = pair[1]
            contained += [num for num in range(a,b+1)]
        contained = set(contained)
        contained = list(contained)
        
        if left in contained and right in contained:
            if len(needed) == (contained.index(right) - contained.index(left)+1):
                return True
            else:
                return False
        else:
            return False