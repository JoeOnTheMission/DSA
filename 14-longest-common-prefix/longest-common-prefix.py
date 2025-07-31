class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        number_of_words = len(strs)
        letter_to_check_against = ""
        common_prefix = ""
        j = 0
        i = 1
        finished = False
        shortest_string = min(strs, key=len)# Find the string with the minimum length
        least_length = len(shortest_string)# Get the length of the shortest string
        if number_of_words == 1:
            common_prefix = strs[0]
            return common_prefix

        for j in range(least_length):
            first_word = strs[0]
            
            letter_to_check_against = first_word[j]
            for i in range(1,number_of_words):
                word_to_check = strs[i]
                letter_to_check = word_to_check[j]
                if letter_to_check_against == letter_to_check and i == number_of_words - 1:
                    common_prefix = common_prefix + letter_to_check
                    break
                if letter_to_check_against != letter_to_check:
                    finished = True
                    break
            if finished:
                break 
        return common_prefix