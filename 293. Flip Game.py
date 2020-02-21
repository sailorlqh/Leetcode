class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        length = len(s)
        for i in range(0, length - 1):
            if(s[i:i+2] == '++'):
                ans.append(s[:i] + '--' + s[i+2:])
        return ans