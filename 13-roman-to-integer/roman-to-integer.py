class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
                "I" : 1 ,
                "IV" : 4 ,
                "V" : 5 ,
                "IX" : 9 ,
                "X" : 10 ,
                "XL": 40 ,
                "L" : 50 ,
                "XC" : 90 ,
                "C" : 100 ,
                "CD" : 400 ,
                "D" : 500 ,
                "CM" : 900 ,
                "M" : 1000
             }
        num = 0
        iddex_checked = 0
        loop_skipper = ""
        for letter in s:
            if len(loop_skipper) != 0:
                loop_skipper = ""
                continue
            if letter == "I" and s.index(letter) != len(s)-1:
                letter_beside = s[s.index(letter)+1]
                if letter_beside == "V":
                    letter_to_check = letter + letter_beside
                    num = num + d[letter_to_check]
                    loop_skipper = "V"
                elif letter_beside == "X":
                    letter_to_check = letter + letter_beside
                    num = num + d[letter_to_check]
                    loop_skipper = "x"
                else:
                    num = num + d[letter]
            elif letter == "X" and s.index(letter) != len(s)-1:
                letter_beside = s[s.index(letter) + 1]
                if letter_beside == "L":
                    letter_to_check = letter + letter_beside
                    num = num + d[letter_to_check]
                    loop_skipper = "L"
                elif letter_beside == "C":
                    letter_to_check = letter + letter_beside
                    num = num + d[letter_to_check]
                    loop_skipper = "C"
                else:
                    num = num + d[letter]
            elif letter == "C" and s.index(letter) != len(s)-1:
                letter_beside = s[s.index(letter) + 1]
                if letter_beside == "D":
                    letter_to_check = letter + letter_beside
                    num = num + d[letter_to_check]
                    loop_skipper = "D"
                elif letter_beside == "M":
                    letter_to_check = letter + letter_beside
                    num = num + d[letter_to_check]
                    loop_skipper = "M"
                else:
                    num = num + d[letter]
            else:
                num = num + d[letter]
        return num