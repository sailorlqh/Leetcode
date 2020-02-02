class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) == 0):
            return True
        if(len(s) == 1):
            return s in t
        if(len(t) == 0):
            return False
        if(len(s) > len(t)):
            return False
        j = 0
        for i in range(len(s)):
            while(s[i] != t[j]):
                j += 1
                if(j >= len(t)):
                    break
            j += 1
            if(j >= len(t)):
                break
        return i >= len(s)-1
        