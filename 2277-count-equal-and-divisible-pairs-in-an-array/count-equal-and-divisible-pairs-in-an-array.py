class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        num_index = {}
        only_repeated = {}
        def OnlyRepeatedElementIndex(list):
            for index,num in enumerate(list):
                if num in num_index:
                    num_index[num].append(index)
                else:
                    num_index[num] = [index]
            only_repeated = {
                    num : index
                    for num, index in num_index.items()
                        if len(index) > 1
                }
            return  only_repeated
        dic = OnlyRepeatedElementIndex(nums)
        valid_combination = []
        for i in dic.values():
            for x in range(len(i)-1):
                y = x+1
                while y < len(i):
                    valid_combination.append([i[x], i[y]])
                    y = y + 1
        valid = 0
        for value in valid_combination:
            if (value[0]*value[1]) % k == 0:
                valid = valid + 1
        return valid 