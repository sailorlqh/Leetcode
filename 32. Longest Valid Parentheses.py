class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        stack.append(-1)
        lenth = len(s)
        max_lenth = 0
        current_lenth = 0
        for i in range(lenth):
            if(s[i] == '('):
                stack.append(i)   
            else:
                stack.pop()
                if(len(stack) == 0):
                    stack.append(i)
                else:
                    current_lenth = i - stack[len(stack) - 1]
                    max_lenth = max(max_lenth, current_lenth)
        return max_lenth
        

sol = Solution()
a = ")()())"
print(sol.longestValidParentheses(a))