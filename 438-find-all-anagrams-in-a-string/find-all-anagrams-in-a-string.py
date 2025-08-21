class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict
        if len(p)>len(s):
            return []

        l = 0
        r = l + len(p)
        target = defaultdict(int)
        current_subarray = defaultdict(int)
        res = []
        for item in p:
            target[item] += 1

        for i in range(len(p)):
            current_subarray[s[i]] += 1

        while l <= len(s) - len(p):
            valid = 0
            #print(l,r, "first" ,current_subarray)
            for letter in  current_subarray:
                #print(letter,target[letter])
                if letter in target:
                    if  current_subarray[letter] == target[letter]:
                        valid += 1

            if valid == len(target):
                #print(l,current_subarray)
                res.append(l)

            if l == len(s) - len(p):
                current_subarray[s[l]] -= 1
                if current_subarray[s[l]] == 0:
                    del current_subarray[s[l]]
                l += 1
                r = l + len(p)

            else:
                current_subarray[s[r]] += 1
                current_subarray[s[l]] -= 1
                if current_subarray[s[l]] == 0:
                    del current_subarray[s[l]]
                l += 1
                r = l + len(p)
            print(l, "then", current_subarray)
        return res