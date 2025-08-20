class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[0] > nums2[0]:
            nums2,nums1 = nums1,nums2

        d = {num: 0 for num in nums2}
        for i in nums1:
            if i in d:
                return i
        return -1 