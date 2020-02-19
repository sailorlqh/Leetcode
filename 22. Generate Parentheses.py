#use recresive to solve this problem
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def addstr(input_str, left_num, right_num):
            if(left_num + right_num == 2 * n):
                print(input_str)
                result.append(input_str)
            elif(left_num == right_num and left_num < n):
                addstr(input_str+'(', left_num+1, right_num)
            else:
                if(left_num < n):
                    addstr(input_str + '(', left_num+1, right_num)
                    addstr(input_str + ')', left_num, right_num + 1)
                else:
                    addstr(input_str + ')', left_num, right_num + 1)
        i_str = ''
        addstr(i_str, 0, 0)
        return result
                
        