class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        length = len(s)
        if(length % 2 == 1):
            return False
        if(length == 0):
            return True
        for i in range(length):
            if(s[i] == '(' or s[i] == '{' or s[i] == '['):
                stack.append(s[i])
            elif(len(stack) == 0):
                return False
            elif(s[i] == ')'):
                if(stack.pop() != '('):
                    return False
            elif(s[i] == ']'):
                if(stack.pop() != '['):
                    return False
            elif(s[i] == '}'):
                if(stack.pop() != '{'):
                    return False
        if(len(stack) != 0):
            return False
        else:
            return True