class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        answer = 0
        queue = []
        num = a[s[0]]
        queue.append(num)
        answer += num
        for i in range(1, len(s)):
            num = a[s[i]]
            answer += num
            prev = queue.pop()
            queue.append(num)
            if(prev< num):
                answer -= 2 * prev
        return answer
            
        