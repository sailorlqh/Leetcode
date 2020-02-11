class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = {}
        left = 0
        length = len(s)
        if(length == 1):
            return 1
        if(length == 0):
            return 0
        max_length = 1
        hash_table[s[0]] = 0
        for i in range(left+1, length):
            if(s[i] in hash_table.keys() and hash_table[s[i]] >= left):
                # temp_length = i - hash_table[s[i]]
                max_length = max(max_length, i - hash_table[s[i]])
                left = hash_table[s[i]] + 1
                hash_table[s[i]] = i
                i = left
            else:
                hash_table[s[i]] = i
                # temp_length = i - left + 1
                max_length = max(max_length, i - left + 1)
        return max_length
                