class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if(len(nums1) == 0 and len(nums2) > 0):
        	return nums2[len(nums2)/2] if len(nums2) % 2 == 1 else (nums2[len(nums2)/2-1]+nums2[int(len(nums2)/2)])/2.0
        if(len(nums2) == 0 and len(nums1) > 0):
        	return nums1[len(nums1)/2] if len(nums1) % 2 == 1 else (nums1[len(nums1)/2-1]+nums1[int(len(nums1)/2)])/2.0
        if(len(nums1) > len(nums2)):
        	return self.findMedianSortedArrays(nums2, nums1)
        length1 = len(nums1)
        length2 = len(nums2)
        iMin = 0
        iMax = length1
        max_left = None
        max_right = None
        while(iMin <= iMax):
        	i = (iMin + iMax)/2
        	j = (length1 + length2 + 1) / 2 - i
        	if(i < length1 and j > 0 and nums1[i] < nums2[j-1]):
        		iMin = i + 1
        	elif(i > 0 and j < length2 and nums2[j] < nums1[i-1]):
        		iMax = i - 1
        	else:
        		if(i == 0):
        			max_left = nums2[j-1]
        		elif(j == 0):
        			max_left = nums1[i-1]
        		else:
        			max_left = max(nums1[i-1], nums2[j-1])
        		break
        if((length1 + length2) % 2 != 0):
        	return max_left

        if (i == length1):
        	min_right = nums2[j]
        elif(j == length2):
        	min_right = nums1[i]
        else:
        	min_right = min(nums1[i], nums2[j])
        return (max_left + min_right)/2.0

sol = Solution()
a = [1,3]
b = [2]
print(sol.findMedianSortedArrays(a,b))