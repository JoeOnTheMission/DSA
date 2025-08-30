class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
                
        count = [0]* (n + 1)
        for start,end,seat in bookings:
            count[start-1] += seat
            count[end] -= seat
        res = []
        total = 0
        i = 0
        while i < len(count)-1:
            total += count[i]
            res.append(total)
            i += 1
        return res