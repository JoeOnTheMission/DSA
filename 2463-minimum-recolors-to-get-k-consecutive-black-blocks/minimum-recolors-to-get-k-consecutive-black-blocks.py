class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_counter = 0
        for i in range(k):
            if blocks[i] == "W":
                w_counter += 1

        m = w_counter


        for l in range(1, len(blocks) - k + 1):
            r = l + k - 1

            if blocks[l - 1] == "W":
                w_counter -= 1
            if blocks[r] == "W":
                w_counter += 1

            m = min(m, w_counter)
        return m