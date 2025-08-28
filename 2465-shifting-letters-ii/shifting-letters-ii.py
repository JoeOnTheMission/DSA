class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0]*(len(s)+1)
        for l,r,d in shifts:
            if d == 1:
                arr[l] += d
                arr[r+1] -= d
            else:
                arr[l] -= 1
                arr[r + 1] += 1
     
        for i in range(1,len(arr)):#
            arr[i] += arr[i-1]
    
        res = [""]*len(s)
        for j in range(len(s)):
            letter = ord(s[j]) + arr[j]
            while letter < 97:
                letter += 26
            while letter > 122:
                letter -= 26
            res[j]= chr(letter)
        return "".join(res)
    