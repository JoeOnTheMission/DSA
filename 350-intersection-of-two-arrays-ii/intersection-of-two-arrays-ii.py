class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        intersection = set_1.intersection(set_2)
        res = []
        for i in intersection:
            count =min(nums1.count(i),nums2.count(i))
            while count > 0:
                res.append(i)
                count -=1
        return res