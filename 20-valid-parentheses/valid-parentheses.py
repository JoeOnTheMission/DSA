class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        d = {"(":")",
            "[":"]",
            "{":"}"}
        for c in s:
            if c in d:
                seen.append(c)
            else:
                if len(seen) == 0:
                    return False 
                if d[seen[-1]] == c:
                    seen.pop()
                else:
                    return False 
        return True if len(seen) == 0 else False
