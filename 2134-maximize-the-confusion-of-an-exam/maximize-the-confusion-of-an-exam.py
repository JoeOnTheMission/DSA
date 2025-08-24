class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        l = 0
        window = []
        t_counter = 0
        f_counter = 0
        res = 0
        for r in range(len(answerKey)):
            if answerKey[r] == "T":
                t_counter += 1
            else:#its false
                f_counter += 1
            while min(t_counter,f_counter) > k:
                if answerKey[l] == "T":
                    t_counter -= 1
                else:  # its false
                    f_counter -= 1
                l +=1
            res = max(res,r - l + 1)
        return res 