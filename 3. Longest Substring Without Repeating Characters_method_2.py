#this method is faster than the first method
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if(length <= 1):
            return length
        max_str = ''
        max_str += s[0]
        max_length = 1
        for i in range(1, length):
            if(s[i] not in max_str):
                max_str += s[i]
            else:
                max_length = max(max_length, len(max_str))
                max_str = max_str[max_str.index(s[i])+1:]
                max_str += s[i]
        max_length = max(max_length, len(max_str))
        return max_length
                