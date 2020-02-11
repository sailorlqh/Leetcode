class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        digit = ['0','1','2','3','4','5','6','7','8','9']
        sign = ['-','+']
        flag = 1
        answer = 0
        int_max = 2**31 - 1
        int_min = -2**31
        length = len(str)
        if(length == 0):
            return 0
        int_max
        pointer = 0
        while(str[pointer] == ' '):
            pointer += 1
            if(pointer >= length):
                return 0
        if(str[pointer] not in digit and str[pointer] not in sign):
            return 0
        if(str[pointer] in sign):
            if(str[pointer] == '-'):
                flag = -1
            pointer += 1
        if(pointer >= length):
            return 0
        while(str[pointer] in digit):
            answer = answer * 10 + int(str[pointer])
            if(answer > int_max):
                if(flag == 1):
                    return int_max
                else:
                    return int_min
                # return int_max is flag == 1 else int_min
            pointer += 1
            if(pointer >= length):
                break
        return answer*flag
        
        
        
        