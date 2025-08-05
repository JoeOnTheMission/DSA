class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {order[i] :i for i in range(len(order))}
        state = True
        j = 1
        for ind in range(len(words) - 1):# gets the words to check
            word = words[ind]
            next_word = words[ind + 1]
            letter_of_word = word[0]
            letter_of_next_word = next_word[0]
            first = order.index(letter_of_word)
            second = order.index(letter_of_next_word)
            minimum = min(len(word),len(next_word))
            if first == second:
                while first == second:
                    if j > minimum - 1:
                        if len(word) > len(next_word):
                            state= False
                            break
                        elif len(word) == len(next_word):
                            state = True
                            break    
                        else:
                            break
                    letter_of_word = word[j]
                    letter_of_next_word = next_word[j]
                    first = order.index(letter_of_word)
                    second = order.index(letter_of_next_word)
                    if first == second:
                        j = j + 1
                        continue
                    elif first > second:
                        state = False
                    else:
                        continue

            elif first > second:
                state = False
            else:
                continue
        return state