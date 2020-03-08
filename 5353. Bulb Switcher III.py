import numpy as np
class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        num_blub = len(light)
        count = 0
        if(num_blub == 0 or num_blub == 1):
            return num_blub
        prev_blub = []
        # behind_blub = []
        behind_blub = {}
        prev_index = 0
        for i in range(num_blub):
            if(light[i] -1 != prev_index):
                if(light[i] - 1 in behind_blub.keys() and light[i] + 1 in behind_blub.keys()):
                    behind_blub[light[i]-1] += 1 + behind_blub[light[i] + 1]
                    behind_blub.pop(light[i] + 1)
                elif(light[i] - 1 in behind_blub.keys()):
                    behind_blub[light[i]-1] += 1
                elif(light[i] + 1 in behind_blub.keys()):
                    behind_blub[light[i]] = 1 + behind_blub[light[i] + 1]
                    behind_blub.pop(light[i] + 1)
                else:
                    behind_blub[light[i]] = 1
            else:
                prev_index = light[i]
                while(prev_index + 1 in behind_blub):
                    prev_index += behind_blub.pop(prev_index+1)
                if(len(behind_blub) == 0):
                    count += 1


        
        return count
        
        
sol = Solution()
a = [1,8,3,4,9,6,7,2,5,10]
print(sol.numTimesAllBlue(a))