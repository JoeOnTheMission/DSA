class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""
        i = 0
        j = 0
        maxim = max(len(word1), len(word2))
        for some in range(maxim):
            if i > len(word1) - 1 and not j > len(word2) - 1:
                out = out + word2[j]
            elif j > len(word2) - 1 and not i > len(word1) - 1:
                out = out + word1[i]
            else:
                out = out + word1[i] + word2[j]
            i = i + 1
            j = j + 1
        return out