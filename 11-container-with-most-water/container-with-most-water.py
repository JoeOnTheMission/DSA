class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)- 1
        area = 0 
        while l < r:
            res = min(height[l], height[r]) * (r - l)
            area = max(res,area)
            if height[r] < height[l]: #the right one is smaller, push right
                r -= 1
            else:#the left one is smaller, push left
                l += 1
           
        return area
