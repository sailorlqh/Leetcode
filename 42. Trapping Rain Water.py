#use two pointer to solve this problem
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        left = 0
        right = length - 1
        left_max = 0
        right_max = 0
        ans = 0
        while left < right:
            if(height[left] < height[right]):
                if(height[left] >= left_max):
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if(height[right] >= right_max):
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans
                    
            
        