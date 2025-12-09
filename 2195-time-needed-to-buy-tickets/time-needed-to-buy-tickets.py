class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for index, count in enumerate(tickets):
            queue.append([index, count])
            
        time = 0
        
        while queue:
            person_index, tickets_left = queue.popleft()
            tickets_left -= 1
            time += 1
            if person_index == k and tickets_left == 0:
                return time
                            
            if tickets_left > 0:
                queue.append([person_index, tickets_left])
        return time