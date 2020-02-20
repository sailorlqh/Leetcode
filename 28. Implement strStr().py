class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length1 = len(haystack)
        length2 = len(needle)
        
        for i in range(length1 - length2 + 1):
            if(haystack[i:i+length2] == needle):
                return i
        return -1
        