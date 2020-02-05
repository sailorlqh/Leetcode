class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if(stones[1] != 1):
            return False
        num = len(stones)
        # print(num)
        # dp = [[] for j in range(num)]
        avaiable_step = [[] for j in range(num)]
        # dp[1].append(1)
        avaiable_step[1].append(1)
        avaiable_step[1].append(0)
        avaiable_step[1].append(2)
        # print(avaiable_step)
        for i in range(1, num-1):
            # max_value = max(dp[i])
            # if(max_value == 0):
                # return False
            # print('max_value: ', max_value)
            for j in range(i+1, num):
                temp = stones[j]-stones[i]
                if(temp in avaiable_step[i]):
                	# dp[j][i] = temp
                	# dp[j].append(temp)
                	avaiable_step[j].append(temp)
                	avaiable_step[j].append(temp+1)
                	if(temp - 1 >= 0):
                		avaiable_step[j].append(temp - 1)
                # for element in dp[i]:
                # 	if element == 0:
                # 		continue;
                # 	elif(temp in [element - 1, element, element + 1]):
                # 		dp[j][i] = temp
        # self.print_dp(dp)
        if(len(avaiable_step[-1]) > 0):
            return True
        else:
            return False

    def print_dp(self, a):
        for i in range(len(a)):
            print(a[i])
sol = Solution()
a = [[0,1,3,6,10,13,15,18],[0,1,3,6,10,15,16,21],[0,1,3,5,6,8,12,17],[0,1,2,3,4,8,9,11]]
# print(len(a))
for i in range(len(a)):
    print(sol.canCross(a[i]))
