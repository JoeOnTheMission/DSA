class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:   
        first = float('inf')
        second = float('inf')
        state = False
        for n in nums:
            if first >= n:
                first = n 
            elif second >= n: #first  < n 
                second = n 
            else:#first < second < n 
                state =  True
        return state