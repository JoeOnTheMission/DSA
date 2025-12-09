from collections import deque
class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue = deque()
        seen = set()
        seen_and_removed = set()
        for letter in s:
            if letter not in seen:  
                seen.add(letter)
                queue.append(letter)
            else:
                if letter not in seen_and_removed:
                    queue.remove(letter)
                    seen_and_removed.add(letter)            
        return s.index(queue[0]) if queue else -1
