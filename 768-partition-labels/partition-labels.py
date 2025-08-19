class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for letter in s:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        i = 0
        res = []

        while i < len(s):
            current_length = 0
            current = [s[i]]
            count = d[s[i]]
            while True:
                if count == 0:
                    break
                if s[i] in current:
                    count -= 1
                else:
                    count += d[s[i]]
                    count -= 1
                    current.append(s[i])
                i += 1
                current_length += 1
            res.append(current_length)

            if i > len(s):
                break
        return res