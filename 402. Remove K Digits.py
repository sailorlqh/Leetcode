#use stack
#whenever there is a element less than the top element in the stack
#we pop the top element 
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        length = len(num)
        expected_length = length - k
        if(length == k):
            return '0'
        count_zero = num.count('0')
        if(count_zero + k == length):
            return '0'
        stack = []
        ans = ''
        for i in range(length):
            if(len(stack) == 0):
                stack.append(num[i])
            elif(len(stack) + len(num[i:]) == expected_length):
                ans = num[i:]
                break
            elif(stack[-1] > num[i]):
                while(len(stack) != 0 and stack[-1] > num[i]):
                    stack.pop()
                    if(len(stack) + len(num[i:]) == expected_length):
                        ans = num[i:]
                        break
                stack.append(num[i])
            else:
                stack.append(num[i])
        while(len(stack) != 0):
            ans = stack.pop() + ans
        ans = str(int(ans))
        if(len(ans) > expected_length):
            ans = ans[:expected_length]
        return ans
            
        