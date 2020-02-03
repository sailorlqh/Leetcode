class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
        	for j in range(1, i+1):
        		dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]



sol = Solution()
a = 3
print(sol.numTrees(a))
#需要枚举从1-n中的每一个数字作为BST的root的情况
#而BST的可能形式只和输入的数字的多少有关，也就是说
#[1, 2, 3]和[3,4,5]的可能的形式是一样的
#所以对于一个BST，他的可能的形式等于左子树的可能的形式*右子树的可能的形式
#所以只需要计算出从长度为0到长度为n的的BST的形式就可以了
#用递归的方式就可以解决