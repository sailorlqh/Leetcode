class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        temp = list(str(N))
        i = 0
        index = -1
        length = len(temp)
        for i in range(1, length):
            if(temp[i-1] > temp[i]):
                index = i
                break
        if(i == length - 1 and i != index):
            return N
        for j in range(i, 0, -1):
            if(temp[j] < temp[j-1]):
                temp[j-1] = str(int(temp[j-1]) - 1)
                index -= 1
            else:
                break
        ans = temp[0:index+1]
        ans_len = len(ans)
        for i in range(length - ans_len):
            ans += '9'
        return int(''.join(ans))
            
                
        