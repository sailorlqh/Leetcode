#What a stupid question
#To understand the question is much harder than solving the problem
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans = 0
        length = len(A[0])
        len_A = len(A)
        for i in range(length):
            for j in range(1, len_A):
                if(A[j][i] < A[j-1][i]):
                    ans += 1
                    break
        return ans