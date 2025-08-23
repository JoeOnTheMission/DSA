class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        window = {fruits[l]:1}
        res = 1
        for r in range(1,len(fruits)):
            window[fruits[r]] = window.get(fruits[r],0) + 1
            while len(window) > 2: #because each basket is one type

                window[fruits[l]] = window.get(fruits[l], 0) - 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l+=1
            if sum(window.values())> res:
                res = sum(window.values())


        return res