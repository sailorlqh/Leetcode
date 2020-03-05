class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        ans = [0 for i in range(length + 1)]
        for op in updates:
            # op = updates[i]
            start = op[0]
            end = op[1]
            inc = op[2]
            ans[start] += inc
            ans[end+1] -= inc
        for i in range(1, length+1):
            ans[i] += ans[i-1]
        return ans[:length]
        