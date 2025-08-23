class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        marked_dict = {}
        marker = 0
        for group in nums:
            for num in group:
                marked_dict.setdefault(num, []).append(marker)
            marker += 1
        sorted_list = sorted(marked_dict.keys())

        window = {}
        l = 0
        out = []
        res = []
        cal = float('inf')

        for r in range(len(sorted_list)):

            for group_id in marked_dict[sorted_list[r]]:
                window[group_id] = 1 + window.get(group_id, 0)
                
            while len(window) == len(nums):
                a = sorted_list[l]
                b = sorted_list[r]
                if b - a < cal:
                    cal = b - a
                    res = [a, b]
                elif b - a == cal:
                    if a < res[0]:
                        res = [a, b]
                for group_id in marked_dict[sorted_list[l]]:
                    window[group_id] = window.get(group_id, 0) - 1
                    if window[group_id] == 0:
                        del window[group_id]
                l += 1



        return res
