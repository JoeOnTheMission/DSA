class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increasing = True
        decreasing = False
        i = 0
        inflection_point = 0
        state = True
        if len(arr) < 3:
            return False
        if arr[0] > arr[1]:
            return False

        while i < len(arr) - 1:
            if arr[i] == arr[i+1]:
                state = False

            elif increasing:
                if arr[i] > arr[i+1]:
                    increasing = False
                    decreasing = True
                    inflection_point += 1
            elif decreasing:
                if arr[i] < arr[i+1]:
                    increasing = True
                    decreasing = False
                    inflection_point += 1
            i += 1
        if inflection_point ==  1 and state == True:
            state = True
        else:
            state = False
        return state