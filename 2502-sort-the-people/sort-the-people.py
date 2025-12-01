class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_name = {}

        for height, name in zip(heights, names):
            height_to_name[height] = name

        min_index = 0
        while min_index < len(heights):
            for i in range(min_index + 1,len(heights)):
                if heights[min_index] < heights[i]:
                    heights[min_index], heights[i] = heights[i], heights[min_index]
            min_index += 1
        res =  []
        for height in heights:
            res.append(height_to_name[height])
        return res 