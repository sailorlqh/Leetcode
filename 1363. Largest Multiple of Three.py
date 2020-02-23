class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        def form_number(new_digit, nums, length):
            ans = ''
            for i in range(length - 1, -1, -1):
                if(i not in nums):
                    ans += str(new_digit[i])
            return str(int(ans)) if ans != '' else ''
        new_digit = sorted(digits, key = lambda x:x)
        num = []
        a = {}
        key = None
        length = len(new_digit)
        digit_sum = sum(new_digit)
        if(digit_sum % 3 == 0):
            return form_number(new_digit, [-1], length)
        temp_digit = digit_sum % 3
        if(temp_digit == 1):
            for i in range(length):
                if(new_digit[i] % 3 == 1):
                    num = [i]
                    return form_number(new_digit, [i], length)
            count = 0
            for i in range(length):
            	if(new_digit[i] % 3 == 2):
            		num.append(i)
            		count += 1
            		if(count == 2):
            			return form_number(new_digit, num, length)
        if(temp_digit == 2):
            for i in range(length):
                if(new_digit[i] % 3 == 2):
                    num = [i]
                    return form_number(new_digit, [i], length)
            count = 0
            for i in range(length):
                if(new_digit[i] % 3 == 1):
                    count += 1
                    num.append(i)
                    if(count == 2):
                        return form_number(new_digit, num, length)
        return ""