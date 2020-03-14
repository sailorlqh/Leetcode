class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num1_length = len(num1)
        num2_length = len(num2)
        if(num1_length == 0 or num2_length == 0):
        	return '0'

        result = [0] * (num1_length + num2_length)
        
        for i in range(num1_length - 1, -1, -1):
            for j in range(num2_length -1, -1, -1):
                result[i+j+1]+=string.digits.index(num1[i])*string.digits.index(num2[j])
                result[i+j]+=result[i+j+1]//10
                result[i+j+1]=result[i+j+1]%10

        return "".join(str(x) for x in result[ next((i for i,x in enumerate(result) if x!=0),len(result)):]) or "0"