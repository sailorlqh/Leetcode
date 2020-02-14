class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        if(length <= 2):
            return arr[0]
        nums = int(length * 0.25)
        for i in range(length):
            if(arr[i] == arr[i+nums]):
                return arr[i]
        
        