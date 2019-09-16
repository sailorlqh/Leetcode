class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lenth = len(height)
        i = 0
        j = lenth - 1
        max_area = -1
        while(i < j):
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
            if(height[i] <= height[j]):
                i += 1
            else:
                j -= 1
        return max_area