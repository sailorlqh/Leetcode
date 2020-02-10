class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = ['' for i in range(numRows)]
        length = len(s)
        if(length == 0):
            return ''
        if(length == 1 or numRows == 1):
            return s
        index = 0
        flag = True
        while(flag):
            rows[0] += s[index]
            index += 1
            if(index >= length):
                flag = False
                break
            for i in range(1, numRows,1):
                if(not flag):
                    break
                rows[i] += s[index]
                index += 1
                if(index >= length):
                    flag = False
            for i in range(numRows-2, 0, -1):
                if(not flag):
                    break
                rows[i] += s[index]
                index += 1
                if(index >= length):
                    flag = False
        answer = ''
        for i in range(numRows):
            answer += rows[i]
        return answer
            
            

sol = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(sol.convert(s, numRows))