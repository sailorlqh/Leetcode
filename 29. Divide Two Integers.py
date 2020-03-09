class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        flag = 0
        if(dividend < 0):
            flag += 1
        if(divisor < 0):
            flag += 1
        if(dividend > 0):
            dividend = -dividend
        if(divisor > 0):
            divisor = -divisor
        if(divisor == -1):
            return dividend if flag == 1 else -dividend
        count = 0
        while(divisor >= dividend):
            temp = -1
            value = divisor
            while value + value >= dividend:
                value += value
                temp += temp
            count += temp
            dividend -= value
        return count if flag == 1 else -count
            
        