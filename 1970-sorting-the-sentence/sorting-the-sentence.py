class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split()
        another = ["0"]*(len(l)+1)
        for word in l:
            i = int(word[-1])
            another[i] = word[:len(word)-1]
        res = " ".join(another[1:])
        return res