class Solution:
    def printVertically(self, s: str) -> List[str]:
        output = []
        separated_words = s.split(" ")
        maximum = len(max(separated_words, key=len))
        d = {i :"" for i in range(maximum)}
        for word in separated_words:
            for j in range(maximum):
                if j < len(word):
                    letter = word[j]
                    key = j
                    d[key] += letter
                elif j >= len(word):
                    key = j
                    d[key] += " "
        for x in range(maximum):
            letter_to_append = d[x]
            while letter_to_append.endswith(" "):
                letter_to_append = letter_to_append[:-1]
            output.append(letter_to_append)
        return output