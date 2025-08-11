class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
            min_index = 0
            while min_index < len(heights):
                for i in range(min_index + 1,len(heights)):
                    if heights[min_index] < heights[i]:
                        temp = heights[min_index]
                        heights[min_index] = heights[i]
                        heights[i ] = temp

                        temp = names[min_index]
                        names[min_index] = names[i]
                        names[i] = temp

                min_index = min_index + 1
            return names