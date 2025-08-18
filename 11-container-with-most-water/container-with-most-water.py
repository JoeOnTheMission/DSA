class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)- 1
        area = (r - l) * min(height[r],height[l])
        while l < r:
            if min(height[r],height[l]) == height[r]: #the right one is smaller, push right
                r -= 1
            else:#the left one is smaller, push left
                l += 1
            if (r - l) * min(height[r],height[l]) > area:
                area = (r - l) * min(height[r],height[l])
        return area
