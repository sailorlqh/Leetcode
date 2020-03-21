class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        def valid(choose, last):
            if(used[choose]):
                return False
            if(choose + last) % 2 == 1:
                return True
            if(choose + last) // 2 == 4:
                return used[(choose + last) // 2]
            if(choose % 3 != last % 3 and choose // 3 != last // 3):
                return True
            return used[(choose + last) // 2]
        
        def find(last_digit, choose_digit, length):
            count = 0
            if(length == 0):
                return 1
            elif(last_digit == None):
                for i in range(9):
                    if(valid(i, choose_digit)):
                        # print('fuck', choose_digit)
                        used[i] = True
                        count += find(choose_digit, i, length-1)
                        used[i] = False
            else:
                for i in range(9):
                    if(valid(i, choose_digit)):
                        used[i] = True
                        count += find(choose_digit, i, length-1)
                        used[i] = False
            return count
        ans = 0
        for i in range(m, n+1):
            used = [False] * 9
            used[0] = True
            ans += find(None, 0, i-1) * 4 
            used[0] = False
            # print(ans)
            
            used[1] = True
            ans += find(None, 1, i-1) * 4 
            used[1] = False
            # print(ans)
            
            used[4] = True
            ans += find(None,4, i-1)
            used[4] = False
            # print(ans)
        return ans
        