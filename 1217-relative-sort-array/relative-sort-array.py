class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {num : i for i,num in enumerate(arr2) }
        res = []
        extra = []
        count = [0]*len(arr2)
        for num in arr1:
            if num in d:
                count[d[num]] += 1
            else:
                extra.append(num)
        extra.sort()
        for j in range(len(count)):
            frequency =count[j]
            number = arr2[j]
            while frequency:
                res.append(number)
                frequency -= 1
        res.extend(extra)
        return res