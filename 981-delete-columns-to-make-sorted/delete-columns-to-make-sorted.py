class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        number_of_words = len(strs)
        number_of_letter = len(strs[0])
        d ={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        count = 0
        for i in range(number_of_letter):
            for j in range(number_of_words-1):
                first = strs[j][i]
                second = strs[j+1][i]
                first_index = d[first]
                second_index = d[second]
                if first_index > second_index:
                    count = count + 1
                    break
        return count 