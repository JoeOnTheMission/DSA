class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        now = []
        res = []
        for j in image:
            x = j[::-1]
            for num in x:
                if num == 1:
                    now.append(0)
                else:
                    now.append(1)
            res.append(now)
            now = []
        return res