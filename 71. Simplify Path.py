class Solution:
    def simplifyPath(self, path: str) -> str:
        arrs = path.split('/')
        # print(arrs)
        ans = []
        for i in range(len(arrs)):
            # print(arrs[i])
            if(arrs[i] == '..'):
                if(len(ans) != 0):
                    ans.pop()
            elif(arrs[i] == '.' or arrs[i] == ''):
                continue
            else:
                ans.append(arrs[i])
            # print(ans)
        result = '/'
        for i in range(len(ans)):
            result += ans[i]
            if(result[-1] != '/'):
                result += '/'
        if(result[-1] == '/' and len(result) != 1):
            return result[:-1]
        else:
            return result
        