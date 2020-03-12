class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = {}
        b = {}
        for i in range(len(nums1)):
            if(nums1[i] not in a.keys()):
                a[nums1[i]] = 1
        for j in range(len(nums2)):
            if(nums2[j] in a.keys()):
                b[nums2[j]] = 1
        return b.keys()
                
        