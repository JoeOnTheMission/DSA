class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
            n = 0
            while n < len(heights):
                for i in range(len(heights)-1):
                    x = heights[i]
                    y = heights[i+1]
                    if x < y:
                        temp = heights[i]
                        heights[i] = heights[i+1]
                        heights[i+1] = temp

                        temp = names[i]
                        names [i] = names[i+1]
                        names[i+1] = temp

                n = n + 1
            return names