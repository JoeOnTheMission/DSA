class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  
        pairs = []
        l, r = 0, len(people) - 1

        while l <= r:
            current = [people[r]]  
            r -= 1
            if l <= r and current[0] + people[l] <= limit:  
                current.append(people[l])
                l += 1
            pairs.append(current)
        return len(pairs)