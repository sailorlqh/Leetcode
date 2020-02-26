class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def dict_a_leq_dict_b(a, b):
            if(len(a) < len(b)):
                return True
            for key in b.keys():
                if(a[key] < b[key]):
                    return True
            return False

        if(len(s) == 0 or len(t) == 0):
            return ""
        if(s == t):
            return t
        if(t in s):
            return t
        t_dict = {}
        s_dict = {}
        for i in range(len(t)):
            t_dict[t[i]] = t.count(t[i])
        left = 0
        right = 0
        length = len(s)
        min_length = 1000000
        ans = None
        flag = False
        to_the_end_flag = False
        if(s[0] in t):
            s_dict[s[0]] = 1
        while(right < length):
            if(dict_a_leq_dict_b(s_dict, t_dict)):
                right += 1
                if(right == length):
                    if(flag == True):
                        to_the_end_flag = True
                    break
                if(s[right] in t):
                    if(s[right] in s_dict.keys()):
                        s_dict[s[right]] += 1
                    else:
                        s_dict[s[right]] = 1
            else:
                flag = True
                temp_length = right - left + 1
                if(temp_length < min_length):
                    ans = s[left:right+1]
                    min_length = temp_length
                if(s[left] in s_dict.keys()):
                    s_dict[s[left]] -= 1
                left += 1
        if(not dict_a_leq_dict_b(s_dict, t_dict)):
            flag = True
        if(flag == False):
            return ''
        print(right == length)

        while(not dict_a_leq_dict_b(s_dict, t_dict)):
            temp_length = right - left + 1
            if(temp_length < min_length):
                ans = s[left:right+1]
                min_length = temp_length
            if(s[left] in s_dict.keys()):
                s_dict[s[left]] -= 1
            left += 1
        return ans





