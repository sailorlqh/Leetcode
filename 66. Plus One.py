class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        if(digits[-1] != 9):
            digits[-1] += 1
            return digits
        else:
            i = length - 1
            while(i >= 0 and digits[i] == 9):
                digits[i] = 0
                if(i - 1 < 0):
                    return [1] + digits
                i -= 1
            digits[i] += 1
            return digits
        