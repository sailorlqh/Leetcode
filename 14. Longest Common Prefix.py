class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        if(length == 0):
            return ""
        prefix = strs[0]
        for i in range(1, length):
            if(len(prefix) > len(strs[i])):
                prefix = prefix[:len(strs[i])]
            if(len(prefix) == 0):
                return ""
            for j in range(min(len(prefix), len(strs[i]))):
                if(strs[i][j] != prefix[j]):
                    prefix = strs[i][:j]
                    if(len(prefix) == 0):
                        return ""
                    break
            # prefix = prefix[:j]
        return prefix
        