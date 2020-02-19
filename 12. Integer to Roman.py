class Solution(object):
    def intToRoman(self, nums):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        count = 0
        chars = [['I','V','X'],
                 ['X','L','C'],
                 ['C','D','M'],
                ['M']]
        while(nums != 0):
            temp = nums % 10
            nums = nums/10
            
            if(temp == 4):
                result = chars[count][0] + chars[count][1] + result
            elif(temp == 9):
                result = chars[count][0] + chars[count][2] + result
            else:
                if(temp >= 5):
                    flag = temp - 5
                    result = chars[count][1] + chars[count][0]*flag + result
                else:
                    result = chars[count][0] * temp + result
            count += 1
        return result        