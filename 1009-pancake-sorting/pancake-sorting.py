class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(k, array):
            arr_to_flip = array[0:k]
            arr_to_flip.reverse()
            array = array[k:len(array)]
            array = arr_to_flip + array
            return array
        res = arr
        counter = 0
        end = len(arr)
        out = []
        while counter < len(arr) - 1:

            index_of_current_max = res.index(max(res[0:end])) #1

            k = index_of_current_max + 1 #2
            res = flip(k,res)
            out.append(k)

            k = end #3
            end -= 1
            res = flip(k,res)
            out.append(k)

            counter += 1
        return out 