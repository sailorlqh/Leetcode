from collections import Counter
class Solution:
    def minWindow(self, s, t):

        if len(s) < len(t) or not t or not s:
            return ''
        
        t_dict = Counter(t)

        left, right = 0, 0
        
        require_length = len(t)
        
        ans = None
        
        while right < len(s):
            
            if t_dict[s[right]] > 0:
                require_length -= 1
            t_dict[s[right]] -= 1
            
            right += 1
            
            while require_length == 0:
                if not ans or len(ans) > (right - left):
                    ans = s[left:right]
                t_dict[s[left]] += 1
                
                if s[left] in t and t_dict[s[left]] > 0:
                    require_length += 1
                left += 1
        
        return '' if not ans else ans