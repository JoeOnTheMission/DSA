from collections import deque


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        queue = deque(students)
        current_sandwich_index = 0
        search_times = 0
        while queue:

            current_student = queue.popleft()
            if current_student != sandwiches[current_sandwich_index]:
                queue.append(current_student)
                search_times += 1
            else:
                search_times = 0
                current_sandwich_index += 1
            if search_times >= len(queue):
                return len(queue)