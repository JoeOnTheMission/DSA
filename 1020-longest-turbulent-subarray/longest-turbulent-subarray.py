class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        r = 1
        last_seen = ""
        res = 1
        while r < len(arr):
            if arr[r - 1] > arr[r] and last_seen != ">":
                res = max(res,r - l + 1)
                r += 1
                last_seen = ">"
            elif arr[r - 1] < arr[r] and last_seen != "<":
                res = max(res, r - l + 1)
                r += 1
                last_seen = "<"
            else:
                if arr[r-1]==arr[r]:
                    r = r + 1
                l = r - 1
                last_seen = ""
        return res

