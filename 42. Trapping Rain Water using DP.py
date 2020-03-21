#use DP
#thought the time complicity is sitll O(n), it's actually 3*O(n), and it requre O(n) space
#compared with solution using two pointers, dp method is more slow and space uneffiencient
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        ans = 0
        left_max = [0 for i in range(length)]
        right_max = [0 for i in range(length)]
        if(length == 0 or length == 1):
            return 0
        for i in range(length):
            if(i == 0):
                left_max[i] = height[i]
            else:
                left_max[i] = max(height[i], left_max[i-1])
        for i in range(length-1, -1, -1):
            if(i == length-1):
                right_max[i] = height[i]
            else:
                right_max[i] = max(height[i], right_max[i+1])
        for i in range(length):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans
        
                
                    
            
        