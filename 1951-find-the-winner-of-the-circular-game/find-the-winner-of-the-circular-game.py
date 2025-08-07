class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        l = list(range(1, n + 1))  # [1, 2, 3, 4, 5]
        current_index = 0


        while len(l) > 1:
            remove_index = (current_index + k - 1) % len(l)
            l.pop(remove_index)
            current_index = remove_index

        return l[0]
